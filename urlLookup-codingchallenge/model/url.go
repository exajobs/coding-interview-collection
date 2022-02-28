package model

// URLData hols the information of a URL query
type URLData struct {
	// URL holds the original URL path
	Url string `json:"url"`
	// isSafe returns the result of a proxy query
	IsSafe bool `json:"isSafe"`
}
