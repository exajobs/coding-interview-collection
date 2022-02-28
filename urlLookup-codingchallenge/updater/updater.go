package updater

import (
	"bufio"
	"net/url"
	"os"
	"strings"
	"sync"
	"time"

	"github.com/brecode/urlLookup"
	"github.com/brecode/urlLookup/db"
	"github.com/brecode/urlLookup/model"
	log "github.com/sirupsen/logrus"
)

const (
	defaultDirPath        = "../../blacklist"
	defaultUpdateInterval = 10
)

// Updater defines the data structure for the Updater
type Updater struct {
	Deps

	quit    chan struct{}
	wg      sync.WaitGroup
	urlList map[string]bool
}

// Deps introduces the Updater dependencies
type Deps struct {
	Logger   *log.Logger
	Config   *urlLookup.Config
	DbClient db.API
}

// UpdaterOption defines the option function for Updater
type UpdaterOption func(*Updater)

// UseUpdaterDeps returns UpdaterOption that can inject custom dependencies
func UseUpdaterDeps(ud func(*Deps)) UpdaterOption {
	return func(u *Updater) {
		ud(&u.Deps)
	}
}

// NewUpdater returns a new Updater and empty structs of its types
func NewUpdater(opts ...UpdaterOption) *Updater {

	u := &Updater{}
	u.quit = make(chan struct{})
	u.urlList = make(map[string]bool, 0)
	for _, o := range opts {
		o(u)
	}

	return u
}

// Init reads blacklisted URLs and updates the data tore
func (u *Updater) Init() error {

	dirPath := u.Config.Updater.DirPath
	if dirPath == "" {
		dirPath = defaultDirPath
	}

	updateInterval := u.Config.Updater.TimeInterval
	if updateInterval == 0 {
		updateInterval = defaultUpdateInterval
	}

	// read files for the first time before we go into the n-minute loop
	u.wg.Add(1)
	go u.readFile(dirPath)

	u.wg.Add(1)
	go func() {
		defer u.wg.Done()

		for {
			select {
			case <-u.quit:
				return
			case <-time.Tick(time.Minute * time.Duration(updateInterval)):
				u.wg.Add(1)
				go u.readFile(dirPath)
			}
		}
	}()
	return nil
}

func (u *Updater) Close() error {
	u.Logger.Info("[UPDATER]: Waiting for goroutines to finish before exiting")
	close(u.quit)
	u.wg.Wait()

	return nil
}

func (u *Updater) readFile(d string) {
	defer u.wg.Done()

	// open the directory URL files are stored
	f, err := os.Open(d)
	if err != nil {
		u.Logger.Errorf("[UPDATER]: Failed to open directory of urls, err %s", err)
		return
	}

	// find all the files under the directory
	files, err := f.Readdir(-1)
	f.Close()
	if err != nil {
		u.Logger.Errorf("[UPDATER]: Failed to get the files under the given directory, err %s", err)
		return
	}

	for _, file := range files {
		// todo - add additional check to be valid url file
		// todo - limit file size

		// check if we have updated the db with this file already
		if u.urlList[file.Name()] {
			continue
		}

		f, err := os.Open(d + "/" + file.Name())
		if err != nil {
			u.Logger.Errorf("[UPDATER]: Failed to open URL file, err")
			continue
		}
		defer f.Close()

		lineScanner := bufio.NewScanner(f)
		lineScanner.Split(bufio.ScanLines)

		var lines []string

		for lineScanner.Scan() {
			lines = append(lines, lineScanner.Text())
		}

		for _, line := range lines {
			u.wg.Add(1)
			go u.updateDb(line)
		}

		// when done add it on a map of known files
		u.urlList[file.Name()] = true

	}
}

func (u *Updater) updateDb(l string) {
	defer u.wg.Done()
	if l == "" || l == "-" {
		return
	}

	v, err := url.Parse(l)
	if err != nil {
		u.Logger.Errorf("[UPDATER]: Error while parsing url: %s", err)
	}

	// strip URLs from unnecessary prefix/suffix(es)
	key := strings.TrimPrefix(v.String(), "https://www.")
	key = strings.TrimPrefix(key, "https://")
	key = strings.TrimPrefix(key, "http://www.")
	key = strings.TrimPrefix(key, "http://")
	key = strings.TrimPrefix(key, "www.")
	key = strings.TrimSuffix(key, "/")

	val := &model.URLData{
		Url:    key,
		IsSafe: false,
	}

	err = u.DbClient.Update(val)
	if err != nil {
		u.Logger.Errorf("[UPDATER]: Failed to write to db store: %s", err)
	}
}
