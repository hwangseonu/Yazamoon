package tests

import (
	"github.com/revel/revel/testing"
	"net/url"
)

type ApplyTest struct {
	testing.TestSuite
}

func (t *ApplyTest) Before() {
	println("Set up")
}

func (t *ApplyTest) TestApply() {
	t.PostForm("/apply/apply", url.Values{
		"status": {"외출"},
	})
	t.AssertOk()
}

func (t *ApplyTest) After() {
	println("Tear down")
}

