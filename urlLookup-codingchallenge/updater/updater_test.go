package updater

import (
	"testing"
	"time"

	"github.com/brecode/urlLookup"
	"github.com/brecode/urlLookup/model"
	"github.com/sirupsen/logrus"
)

type MockRedisClient struct {
	Log         *logrus.Logger
	CommitDelay time.Duration
}

func (m *MockRedisClient) Get(string) (*model.URLData, bool) {
	return nil, true
}

func (m *MockRedisClient) Update(*model.URLData) error {
	time.Sleep(m.CommitDelay)
	return nil
}

// TestOperationBasic is intended for testing of the updater code in a debugger
func TestOperationBasic(t *testing.T) {
	logger := logrus.New()
	logger.SetLevel(logrus.DebugLevel)
	cfg := &urlLookup.Config{
		Updater: urlLookup.Updater{
			TimeInterval: 10,
			DirPath:      "../blacklist",
		}}

	updtr := NewUpdater(UseUpdaterDeps(func(d *Deps) {
		d.Logger = logger
		d.DbClient = &MockRedisClient{Log: logger, CommitDelay: time.Second * 2}
		d.Config = cfg
	}))

	if err := updtr.Init(); err != nil {
		t.Errorf("%s", err)
	}

	if err := updtr.Close(); err != nil {
		t.Errorf("%s", err)
	}

}

// TestWrongConfig is intended for testing bogus config of the updater code in a debugger
func TestWrongConfig(t *testing.T) {
	logger := logrus.New()
	logger.SetLevel(logrus.DebugLevel)
	cfg := &urlLookup.Config{
		Updater: urlLookup.Updater{
			TimeInterval: 10,
			DirPath:      "../blacklist",
		}}

	updtr := NewUpdater(UseUpdaterDeps(func(d *Deps) {
		d.Logger = logger
		d.DbClient = &MockRedisClient{Log: logger, CommitDelay: time.Second * 2}
		d.Config = cfg
	}))

	if err := updtr.Init(); err != nil {
		t.Errorf("%s", err)
	}

	if err := updtr.Close(); err != nil {
		t.Errorf("%s", err)
	}

}
