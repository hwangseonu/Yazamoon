package models

import (
	"time"
	"github.com/revel/revel"
	"gopkg.in/mgo.v2/bson"
)

type Time struct {
	Start time.Time `json:"start" bson:"start"`
	End   time.Time `json:"end" bson:"end"`
	Name  string    `json:"name" bson:"name"`
}

func NewSchedule(startHour, startMinute, endHour, endMinute int, name string) {
	s := session.Copy()
	defer s.Close()
	now := time.Now()
	start := time.Date(now.Year(), now.Month(), now.Day(), startHour, startMinute, 0, 0, revel.TimeZone)
	end := time.Date(now.Year(), now.Month(), now.Day(), endHour, endMinute, 0, 0, revel.TimeZone)

	t := Time{
		Start: start,
		End: end,
		Name: name,
	}

	var data map[string]interface{}
	c := s.DB("kysis").C("data")
	c.Find(nil).One(&data)

	if data == nil {
		data = make(map[string]interface{})
		data["time_table"] = make([]string, 0)
		data["feedback"] = make([]string, 0)
	}

	data["time_table"] = append(data["time_table"].([]interface{}), t)
	c.Upsert(bson.M{"_id": data["_id"]}, data)
}

func GetTimeTable() []interface{} {
	s := session.Copy()
	defer s.Close()
	var data map[string]interface{}
	s.DB("kysis").C("data").Find(nil).One(&data)
	timeTable := data["time_table"].([]interface{})
	return timeTable

}