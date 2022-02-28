package router

import (
	"github.com/brecode/urlLookup/handler"
	log "github.com/sirupsen/logrus"

	"github.com/gorilla/mux"
)

// Router defines the data structure for the Router
type Router struct {
	Deps
	*mux.Router
}

// Deps introduces the Router dependencies
type Deps struct {
	Logger  *log.Logger
	Handler handler.API
}

// RouterOption defines the option function for Router
type RouterOption func(*Router)

// UseRouterDeps returns RouterOption that can inject custom dependencies.
func UseRouterDeps(rd func(*Deps)) RouterOption {
	return func(r *Router) {
		rd(&r.Deps)
	}
}

// NewRouter returns a new Router with routes defined in this package
func NewRouter(opts ...RouterOption) *Router {

	r := &Router{}
	for _, o := range opts {
		o(r)
	}

	return r
}

// Init initializes the Router
func (r *Router) Init() error {

	r.Router = mux.NewRouter().StrictSlash(true)

	// a list of routes to be registered
	for _, route := range r.GetRoutes() {
		r.Router.Methods(route.Method).
			PathPrefix(route.Pattern).
			Subrouter().
			Name(route.Name).
			Handler(route.HandlerFunc)
	}

	return nil
}

// Close gracefully stops the Router
func (r *Router) Close() error {
	return nil
}
