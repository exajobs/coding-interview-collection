package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/brecode/urlLookup"
	"github.com/brecode/urlLookup/db"
	"github.com/brecode/urlLookup/model"
	log "github.com/sirupsen/logrus"
)

// Handler defines the data structure for the Handler
type Handler struct {
	Deps
}

// Deps introduces the Handler dependencies
type Deps struct {
	Logger   *log.Logger
	DbClient db.API
}

// HandlerOption defines the option function for Router
type HandlerOption func(*Handler)

// UseHandlerDeps returns HandlerOption that can inject custom dependencies.
func UseHandlerDeps(hd func(*Deps)) HandlerOption {
	return func(h *Handler) {
		hd(&h.Deps)
	}
}

// NewHandler returns a new Handler
func NewHandler(opts ...HandlerOption) *Handler {

	h := &Handler{}
	for _, o := range opts {
		o(h)
	}

	return h
}

// GetURLData will be the handling function for caller's queries (GET)
func (h *Handler) GetURLData() http.HandlerFunc {
	return func(w http.ResponseWriter, req *http.Request) {

		// split the address into URL and URI
		url := strings.Split(req.URL.String(), "/")
		pathAndQuery := strings.Join(url[4:], "/")
		hostAndPort := url[3]

		// get the top level domain and convert it into a sha1 has value
		tld := urlLookup.GetSha(urlLookup.GetTLDPlusOne(hostAndPort))
		h.Logger.Debugf("[HANDLER]: tld key: %x", tld)

		// 1. check if the entire domain is blacklisted, return if found
		if v, found := h.DbClient.Get(fmt.Sprintf("%x", tld)); !found {
			h.Logger.Debugf("[HANDLER]: Domain not found, check for full path")
		} else {
			h.httpResponse(w, v)
			return
		}

		// 2. Check for the full path and query arguments.
		fPath := hostAndPort + "/" + pathAndQuery
		key := urlLookup.GetSha(fPath)
		h.Logger.Debugf("[HANDLER]: db query key: %x", key)

		if v, found := h.DbClient.Get(fmt.Sprintf("%x", key)); !found {
			h.Logger.Debug("[HANDLER]: Key not found, website safe, yay!")
			h.httpResponse(w, v)
			return
		} else {
			h.httpResponse(w, v)
		}

	}
}

// UpdateURLData will be the handling function for caller's Update requests (POST)
func (h *Handler) UpdateURLData() http.HandlerFunc {
	return func(w http.ResponseWriter, req *http.Request) {
		url := &model.URLData{}

		if err := json.NewDecoder(req.Body).Decode(url); err != nil {
			h.Logger.Debugf("[HANDLER]: Failed to decode incoming request, err: %s", err)
			h.httpErrorResponse(w, err)
		} else {
			h.Logger.Debugf("[HANDLER]: Decoded request in JSON  is: %+v", url)
			h.httpResponse(w, nil)
			_ = h.DbClient.Update(url)
		}
	}
}

func (h *Handler) httpResponse(w http.ResponseWriter, v *model.URLData) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	if v == nil {
		_, _ = w.Write([]byte{})
		return
	}

	resp := fmt.Sprintf(`{"isSafe": "%s"}`, strconv.FormatBool(v.IsSafe))
	_, _ = w.Write([]byte(resp))
}

func (h *Handler) httpErrorResponse(w http.ResponseWriter, err error) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusInternalServerError)

	resp := fmt.Sprintf(`{"error": "%s"}`, err)
	_, _ = w.Write([]byte(resp))
}
