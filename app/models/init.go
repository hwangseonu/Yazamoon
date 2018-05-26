package models

import (
	"gopkg.in/mgo.v2"
)

var session *mgo.Session

func init() {
	var err error
	session, err = mgo.Dial("mongodb://localhost:27017")
	if err != nil {
		panic(err)
	}

}
