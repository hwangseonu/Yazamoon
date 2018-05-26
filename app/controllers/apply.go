package controllers

import (
	"github.com/revel/revel"
	"github.com/hwangseonu/Kysis-Hackathon/app/models"
	"strconv"
)

type Apply struct {
	App
}

func (c Apply) Index() revel.Result {
	return c.Render()
}

func (c Apply) Apply(status string) revel.Result {
	if CurrentUser == (models.User{}) {
		return c.Redirect(App.Index)
	}
	class := CurrentUser.StudentID[:3]
	id, _ := strconv.Atoi(CurrentUser.StudentID[3:])

	models.Apply(class, id, status)
	return c.Redirect(Apply.Index)
}
