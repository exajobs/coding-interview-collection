package db

import (
	"encoding/json"
	"fmt"

	"github.com/brecode/urlLookup"
	"github.com/brecode/urlLookup/model"
	"github.com/go-redis/redis"
	log "github.com/sirupsen/logrus"
)

// Database holds the data structure for access to the data store
// Multiple clients can be added here, this exercise will test with redis
type Database struct {
	Deps

	redisClient *redis.Client
}

type Deps struct {
	Logger *log.Logger
	Config *urlLookup.Config
}

// DbOption defines the option function for Database
type DbOption func(*Database)

// UseDbDeps returns DbOption that can inject custom dependencies.
func UseDbDeps(dd func(*Deps)) DbOption {
	return func(d *Database) {
		dd(&d.Deps)
	}
}

// NewDatabase returns a Database
func NewDatabase(opts ...DbOption) *Database {

	d := &Database{}
	for _, o := range opts {
		o(d)
	}

	return d
}

// Init starts the db connection and initializes all the Database types
func (db *Database) Init() error {
	db.redisClient = redis.NewClient(&redis.Options{
		Addr:     db.Config.Address,
		Network:  db.Config.RedisDB.Network,
		Password: db.Config.RedisDB.Password,
		DB:       db.Config.RedisDB.DB,
	})

	// ping to check if connection is active
	_, err := db.redisClient.Ping().Result()

	return err
}

// Close function gets called when main terminates, safely closes the connection to the data stores
func (db *Database) Close() error {
	db.Logger.Infof("[DB]: Closing connection to data store")

	if err := db.redisClient.Close(); err != nil {
		return err
	}

	return nil
}

// Get function queries the data store (redis in this exercise)
func (db *Database) Get(key string) (*model.URLData, bool) {
	db.Logger.Infof("[DB]: Get request for db with key: %s", key)

	r := &model.URLData{}

	val, err := db.redisClient.Get(key).Bytes()
	if err != nil {
		db.Logger.Debugf("[DB]: Could not find key in data store: %+v", err)
		// not really an error, value not in the db => url is safe
		r = &model.URLData{IsSafe: true}
		return r, false
	}

	_ = json.Unmarshal(val, r)

	return r, true
}

// Update calls the redis client api to update the keys in db
func (db *Database) Update(u *model.URLData) error {
	db.Logger.Infof("[DB]: Update request for db with key: %s", u.Url)

	key := urlLookup.GetSha(u.Url)
	dbKey := fmt.Sprintf("%x", key)

	value, err := json.Marshal(u)
	if err != nil {
		db.Logger.Errorf("[DB]: Failed to marshal url data into json: %s", err)
		return err
	}

	err = db.redisClient.Set(dbKey, value, 0).Err()
	if err != nil {
		db.Logger.Errorf("[DB]: Error while trying to update data store: %s", err)
		return err
	}

	return nil
}
