package main

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"net/http"
	"os"
	"os/signal"

	log "github.com/sirupsen/logrus"
	flag "github.com/spf13/pflag"

	"github.com/brecode/urlLookup"
	"github.com/brecode/urlLookup/db"
	"github.com/brecode/urlLookup/handler"
	"github.com/brecode/urlLookup/router"

	"github.com/ghodss/yaml"
)

var (
	address = *flag.StringP("address", "a", "0.0.0.0",
		"The address web service listens at, \n")
	port = *flag.StringP("port", "p", "32697",
		"The port web service listens at, \n")
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
	// starting with redis but in the init one can set a connection for a different data store
	redis := db.NewDatabase(db.UseDbDeps(
		func(deps *db.Deps) {
			deps.Logger = logger
			deps.Config = cfg
		}))
	if err = redis.Init(); err != nil {
		logger.Fatalf("Could not initialize db, exiting with error: %+v", err)
	}

	// create a new handler initialize and inject dependencies
	hndlr := handler.NewHandler(handler.UseHandlerDeps(
		func(deps *handler.Deps) {
			deps.Logger = logger
			deps.DbClient = redis
		}))

	// create a new router initialize and inject dependencies
	rtr := router.NewRouter(router.UseRouterDeps(
		func(deps *router.Deps) {
			deps.Handler = hndlr
			deps.Logger = logger
		}))
	if err = rtr.Init(); err != nil {
		logger.Fatalf("Could not initialize router, exiting with error: %+v", err)
	}

	// go thread to handle interrupt signal
	go handleInterrupt(logger, redis)

	logger.Printf("Starting HTTP service at >> %s:%s\n", address, port)
	logger.Fatal(http.ListenAndServe(address+":"+port, rtr))
}

func handleInterrupt(logger *log.Logger, db *db.Database) {
	// handle interrupt signal
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt)

	for {
		select {
		case <-quit:
			logger.Debugf("[MAIN]: Caught interrupt signal, exiting...")

			// close db connection before exiting, log if fails but still exit with code 1 this time
			if err := db.Close(); err != nil {
				logger.Errorf("Failed to gracefully close db, err: %s", err)
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
