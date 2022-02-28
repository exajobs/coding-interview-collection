package router

import (
	"net/http"
)

// Route holds the information of a CRUD operation sets the route pattern and handling function
type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

// Routes contains multiple route structs
type Routes []Route

func (r *Router) GetRoutes() Routes {
	// a list of routes to register with the router
	return Routes{
		Route{
			Name:        "urlLookUp",
			Method:      "GET",
			Pattern:     "/urlinfo/1/",
			HandlerFunc: r.Handler.GetURLData(),
		},
		Route{
			Name:        "urlUpdate",
			Method:      "POST",
			Pattern:     "/urlupdate/1/updateData",
			HandlerFunc: r.Handler.UpdateURLData(),
		},
	}
}
