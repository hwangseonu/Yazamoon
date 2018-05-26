package controllers

import (
	"github.com/revel/revel"
	"github.com/hwangseonu/Kysis-Hackathon/app/models"
	"net/http"
)

var CurrentUser models.User = (models.User{})

type App struct {
	*revel.Controller
}

var data = models.GetAttendance("100")
var (
	i1 = data[0]
	i2 = data[1]
	i3 = data[2]
	i4 = data[3]
	i5 = data[4]
	i6 = data[5]
	i7 = data[6]
	i8 = data[7]
	i9 = data[8]
	i10 = data[9]
	i11 = data[10]
	i12 = data[11]
	i13 = data[12]
	i14 = data[13]
	i15 = data[14]
	i16 = data[15]
	i17 = data[16]
	i18 = data[17]
	i19 = data[18]
	i20 = data[19]
	i21 = data[20]
	i22 = data[21]
	i23 = data[22]
	i24 = data[23]
	i25 = data[24]
	i26 = data[25]
	i27 = data[26]
	i28 = data[27]
	i29 = data[28]
	i30 = data[29]
	i31 = data[30]
	i32 = data[31]
	i33 = data[32]
	i34 = data[33]
	i35 = data[34]
	i36 = data[35]
	i37 = data[36]
	i38 = data[37]
	i39 = data[38]
	i40 = data[39]
	i41 = data[40]
	i42 = data[41]
)

func (c App) Index() revel.Result {
	if CurrentUser != (models.User{}) {
		return c.Redirect(App.Main)
	} else {
		return c.Render()
	}
}

func (c App) Main(class string) revel.Result {
	if CurrentUser == (models.User{}) {
		return c.Redirect(App.Index)
	} else {
		return c.Render(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39, i40, i41, i42)
	}
}

func (c App) Apply() revel.Result {
	if i23 == "check" {
		c.Flash.Error("이미 출석 체크가 되어 있습니다.")
		return c.Redirect(App.Main)
	}
	i23 = "miss"
	//i20 = "check"
	return c.Redirect(App.Main)
}


func (c App) ApplyOut() revel.Result {
	if i23 == "check" {
		c.Flash.Error("이미 출석 체크가 되어 있습니다.")
		return c.Redirect(App.Main)
	} else if i23 == "gap" {
		c.Flash.Error("야자 신청을 하고 해주세요.")
		return c.Redirect(App.Main)
	}
	i23 = "out"
	return c.Redirect(App.Main)
}

func (c App) Check() revel.Result {
	if i23 == "check" {
		c.Flash.Error("이미 출석 체크가 되어 있습니다.")
		return c.Redirect(App.Main)
	}
	if i23 == "miss" {
		i23 = "check"
	} else {
		c.Flash.Error("먼저 야자신청을 해주세요!")
	}
	return c.Redirect(App.Main)
}

func (c App) TimeTable() revel.Result {
	return c.Render()
}

func (c App) Notice() revel.Result {
	return c.Render()
}

func (c App) Feedback() revel.Result {
	return c.Render()
}

func (c App) SendFeedback(contents string) revel.Result {
	models.NewFeedback(contents, CurrentUser.Username)
	c.Flash.Success("건의사항이 접수되었습니다.")
	return c.Redirect(App.Feedback)
}

func (c *App) SignIn(username, password string) revel.Result {
	if CurrentUser != (models.User{}) {
		return c.Redirect(App.Index)
	}
	user, err := models.GetUser(username, password)
	if err != nil || user == (models.User{}){
		c.Logout()
		c.Flash.Error("잘못된 접근입니다.")
		return c.Redirect(App.Index)
	}
	c.setCurrentUser(user)
	return c.Redirect(App.Index)
}

func (c *App) SignUp(username, password, student_id, school_code string) revel.Result {
	if CurrentUser != (models.User{}) {
		return c.Redirect(App.Index)
	}
	err := models.NewUser(username, password, student_id, school_code)
	if err != nil {
		c.Response.SetStatus(http.StatusUnauthorized)
		c.Flash.Error("회원가입에 실패하였습니다.")
		return c.Redirect(App.Index)
	}
	return c.Redirect(App.Index)
}

func (c *App) Logout() revel.Result {
	CurrentUser = (models.User{})
	for key := range c.Session {
		delete(c.Session, key)
	}
	return c.Redirect(App.Index)
}

func (c *App) setCurrentUser(user models.User) revel.Result{
	CurrentUser = user
	return nil
}
