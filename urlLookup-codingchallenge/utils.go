package urlLookup

import (
	"crypto/sha1"
	"strings"

	"golang.org/x/net/publicsuffix"
)

// GetSha calculates a sha1 hash value
func GetSha(k string) []byte {
	h := sha1.New()
	h.Write([]byte(k))
	bs := h.Sum(nil)

	return bs
}

// GetTLDPlusOne returns the effective top level domain plus one more label.
func GetTLDPlusOne(k string) string {
	h := strings.Split(k, ":")
	v, _ := publicsuffix.EffectiveTLDPlusOne(h[0])

	return v
}
