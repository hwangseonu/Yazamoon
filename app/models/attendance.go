package models

import "gopkg.in/mgo.v2/bson"

type Attendance []string

func Apply(class string, id int, status string) {
	s := session.Copy()
	defer s.Close()

	var cl map[string]interface{}
	c := s.DB("kysis").C("attendance")
	c.Find(bson.M{"class": class}).One(&cl)

	cl["status"].([]interface{})[id-1] = status
	c.Upsert(bson.M{"class": class}, cl)
}

func GetAttendance(class string) []interface{} {
	s := session.Copy()
	defer s.Close()

	var data map[string]interface{}
	c := s.DB("kysis").C("attendance")
	c.Find(bson.M{"class": class}).One(&data)

	return data["status"].([]interface{})
}