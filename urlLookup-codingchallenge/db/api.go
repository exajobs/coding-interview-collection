package db

import "github.com/brecode/urlLookup/model"

// API is the interface for accessing the underlying data store
type API interface {
	// Get returns data information and true/false if the key is found
	Get(key string) (*model.URLData, bool)

	// Update exposes an API to save new data into the data store
	Update(url *model.URLData) error
}
