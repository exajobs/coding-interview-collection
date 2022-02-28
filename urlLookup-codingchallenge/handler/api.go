package handler

import (
	"net/http"
)

// API is the interface for accessing the handler's functions for defined CRUD operations
type API interface {
	// GetUrlInfo is the handler for the query of a malicious URL (GET)
	GetURLData() http.HandlerFunc

	// UpdateUrlInfo is the handler for adding malicious url (POST)
	UpdateURLData() http.HandlerFunc
}
