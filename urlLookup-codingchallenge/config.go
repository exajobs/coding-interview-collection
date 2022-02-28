package urlLookup

// Config holds the system-wide configuration data structure
type Config struct {
	RedisDB `json:"redis"`
	Updater `json:"updater"`
}

// RedisDB holds the configurable types of a redis client connection
type RedisDB struct {
	// The network type, either tcp or unix.
	Network string `json:"network,omitempty"`

	// host:port address
	Address string `json:"address,omitempty"`

	// Optional password. Must match the password specified in the
	// require pass server configuration option.
	Password string `json:"password,omitempty"`

	// Database to be selected after connecting to the server.
	DB int `json:"db,omitempty"`
}

// Updater holds the configurable types of the Updater
type Updater struct {
	// The update interval to upgrade the db (in minutes)
	TimeInterval uint32 `json:"timeInterval,omitempty"`

	// Directory path of disk mapped files with blacklisted URLs
	DirPath string `json:"dirPath,omitempty"`
}
