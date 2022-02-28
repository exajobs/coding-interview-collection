package main

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"os"
	"os/signal"

	"github.com/brecode/urlLookup/updater"
	log "github.com/sirupsen/logrus"
	flag "github.com/spf13/pflag"

	"github.com/brecode/urlLookup"
	"github.com/brecode/urlLookup/db"

	"github.com/ghodss/yaml"
)

var (
	cfgFile = flag.StringP("cfgFile", "c", "",
		"Name of the configuration file\n")
	err error
)

func main() {

	flag.Parse()
	logger := log.New()
	logger.SetLevel(log.DebugLevel)
	cfg := getConfig(logger)

	// create a new database initialize and inject dependencies
	redis := db.NewDatabase(db.UseDbDeps(
		func(deps *db.Deps) {
			deps.Logger = logger
			deps.Config = cfg
		}))
	if err = redis.Init(); err != nil {
		logger.Fatalf("Failed to initialize db, exiting with error: %+v", err)
	}

	updtr := updater.NewUpdater(updater.UseUpdaterDeps(
		func(deps *updater.Deps) {
			deps.DbClient = redis
			deps.Config = cfg
			deps.Logger = logger
		}))
	if err = updtr.Init(); err != nil {
		logger.Fatalf("Failed to initialize updater, exiting with error: %+v", err)
	}

	// go thread to handle interrupt signal
	handleInterrupt(logger, redis, updtr)
}

func handleInterrupt(logger *log.Logger, db *db.Database, updtr *updater.Updater) {
	// handle interrupt signal
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt)
	logger.Info("[UPDATER]: Wait loop")

	for {
		select {
		case <-quit:
			logger.Debugf("[MAIN]: Caught interrupt signal, exiting...")

			// close db connection before exiting, log if fails but still exit with code 1 this time
			if err := db.Close(); err != nil {
				logger.Errorf("Failed to safely close db, err: %s", err)
				os.Exit(1)
			}

			// gracefully close updater before exiting, log if fails but still exit
			if err := updtr.Close(); err != nil {
				logger.Errorf("Failed to gracefully close updater, err: %s", err)
				os.Exit(1)
			}

			os.Exit(0)
		}
	}
}

// GetConfig returns the system-wide configuration from a provided configuration file
// for this exercise config file is on YAML format but that can be extended to more formats (i.e JSON)
func getConfig(logger *log.Logger) *urlLookup.Config {

	if *cfgFile == "" {
		logger.Fatal("DB configuration file not specified, please provide with a configuration file")
	}

	// return the content of the config file
	data, err := ioutil.ReadFile(*cfgFile)
	if err != nil {
		logger.Fatalf("Failed to read configuration file '%s', error %s", *cfgFile, err)
	}

	cfg := &urlLookup.Config{}

	// converts a yaml byte stream into json format
	jsonData, err := yaml.YAMLToJSON(data)
	if err != nil {
		logger.Fatalf("Failed to convert yaml to json, error %s", err)
	}

	// fill the config struct with the decoded values
	jd := json.NewDecoder(bytes.NewReader(jsonData))

	jd.DisallowUnknownFields()
	if err := jd.Decode(cfg); err != nil {
		logger.Fatalf("Failed to unmarshal config data from JSON, error %s", err)
	}

	return cfg
}
