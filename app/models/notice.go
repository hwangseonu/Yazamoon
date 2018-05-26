package models

import "gopkg.in/mgo.v2/bson"

type Notice struct {
	Title	string	`json:"title" bson:"title"`
	Contents string `json:"contents" bson:"contents"`
}

func NewNotice(con,  user string) {
	f := Feedback{
		Contents:con,
		Writer:user,
	}
	s := session.Copy()
	defer s.Close()

	var data map[string]interface{}
	c := s.DB("kysis").C("data")
	c.Find(nil).One(&data)

	data["feedback"] = append(data["feedback"].([]interface{}), f)
	c.Upsert(bson.M{"_id": data["_id"]}, data)
}

func GetNotice() []Notice {
	s := session.Copy()
	defer s.Close()
	var data map[string]interface{}
	return data["feedback"].([]Notice)
}