from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django import forms

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm
from .models import ClassModel, SeatModel

import re


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {
            'login': LoginForm(prefix='login'),
            'register': RegisterForm(prefix='register')
        })


class LoginView(View):
    def post(self, request: HttpRequest):
        form = LoginForm(request.POST, prefix='login')
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)
            if user:
                login(request, user=user)
            else:
                messages.error(request, '아이디나 비밀번호가 일치하지 않습니다.')
        else:
            messages.error(request, form.errors)
        return redirect('index')


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect('index')


class RegisterView(View):
    def post(self, request: HttpRequest):
        form = RegisterForm(request.POST, prefix='register')
        if form.is_valid():
            try:
                user = form.save()
                group, _ = Group.objects.get_or_create(name=user.student_id[:3])
                user.groups.add(group)
                user.save()
                messages.success(request, '회원가입되었습니다.')
            except forms.ValidationError as e:
                messages.error(request, e)
        else:
            messages.error(request, form.errors)
        return redirect('index')


class SeatsView(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        user = request.user

        class_id = user.student_id[:3]
        cls, _ = ClassModel.objects.get_or_create(class_id=class_id)
        seats = [[None] * 5 for _ in range(5)]

        have_seat = False
        for s in cls.seatmodel_set.all():
            if s.student.student_id == user.student_id:
                have_seat = True
            row, column = s.get_position()
            seats[column-1][row-1] = s

        return render(request, 'app/seats.html', {'seats': seats, 'have_seat': have_seat})

    @method_decorator(login_required(login_url='/'))
    def post(self, request):
        pos_regex = re.compile(r"^\d,\d$")
        user = request.user
        pos = request.POST.get("position", None)

        if pos is None or not pos_regex.match(pos):
            return redirect("seats")

        if SeatModel.objects.filter(cls_id=user.student_id[:3], position=pos).exists():
            messages.error(request, "빈 자리를 선택해주세요.")
            return redirect("seats")

        SeatModel.objects.create(student=user, cls_id=user.student_id[:3], position=pos)
        return redirect('seats')


class AttendanceView(View):
    @method_decorator(login_required(login_url='/'))
    def post(self, request):
        user = request.user
        seat = SeatModel.objects.filter(student=user).first()

        if seat is not None:
            if seat.status == 'check':
                messages.error(request, '이미 출석되었습니다.')
            else:
                seat.status = 'check'
                seat.save()
                messages.success(request, '출석되었습니다.')
        else:
            messages.error(request, '등록된 자리가 없습니다.')

        return redirect('seats')
