package tests

import (
	"github.com/revel/revel/testing"
	"net/url"
	"net/http"
)

type AccountTest struct {
	testing.TestSuite
}

func (t *AccountTest) Before() {
	println("Set up")
}

func (t *AccountTest) TestSignUp() {
	t.PostForm("/account/signup", url.Values{
		"username":{"test"},
		"password":{"test"},
		"student_id": {"10101"},
		"school_code": {"0001"},
	})
	if t.Response.StatusCode == http.StatusUnauthorized {
		t.AssertNotFound()
	} else {
		t.AssertOk()
	}
}

func (t *AccountTest) TestSignIn() {
	t.PostForm("/account/signin", url.Values{
		"username":{"test"},
		"password":{"test"},
	})
	if t.Response.StatusCode == http.StatusUnauthorized {
		t.AssertNotFound()
	} else {
		t.AssertOk()
	}
}

func (t *AccountTest) After() {
	println("Tear down")
}
