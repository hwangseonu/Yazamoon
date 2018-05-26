package controllers

import (
	"github.com/revel/revel"
	"github.com/hwangseonu/Kysis-Hackathon/app/models"
)

type Admin struct {
	App
}

func (c Admin) Index() revel.Result {
	return c.Render()
}

func (c Admin) Feedback() revel.Result {
	feedback := models.GetFeedback()
	return c.Render(feedback)
}

func (c Admin) AddFeedback(title, contents string) revel.Result {
	models.NewFeedback(contents, CurrentUser.Username)
	return c.Redirect(Admin.Feedback)
}

func (c Admin) TimeTable() revel.Result {
	timeTable := models.GetTimeTable()
	return c.Render(timeTable)
}

func (c Admin) AddSchedule(start_hour, start_minute, end_hour, end_minute int, name string) revel.Result {
	models.NewSchedule(start_hour, start_minute, end_hour, end_minute, name)
	return c.Redirect(Admin.TimeTable)
}