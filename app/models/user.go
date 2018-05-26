package models

import (
	"gopkg.in/mgo.v2/bson"
	"fmt"
)

type User struct {
	Id        bson.ObjectId `json:"id" bson:"_id"`
	Username  string        `json:"username" bson:"username"`
	Password  string        `json:"password" bson:"password"`
	StudentID string        `json:"student_id" bson:"student_id"`
	School    string        `json:"school" bson:"school"`
}

func (u User) Save() error {
	s := session.Copy()
	defer s.Close()
	err := s.DB("kysis").C("users").Insert(u)
	if err != nil {
		return fmt.Errorf("already exists user")
	}
	return nil
}

func NewUser(un, pw, sid, scode string) error {
	id := bson.NewObjectId()
	school := GetSchoolName(scode)
	user := User{
		Id: id,
		Username: un,
		Password: pw,
		StudentID:sid,
		School: school,
	}
	return user.Save()
}

func GetSchoolName(code string) string {
	if code == "0001" {
		return "한국디지털미디어고등학교"
	} else {
		return "대덕소프트웨어마이스터고등학교"
	}
}

func GetUser(un, pw string) (User, error) {
	var user User
	s := session.Copy()
	defer s.Close()
	err := s.DB("kysis").C("users").Find(bson.M{"username": un, "password": pw}).One(&user)
	if user == (User{}) {
		err = fmt.Errorf("user not found")
	}
	return user, err
}