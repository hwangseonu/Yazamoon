import json

from django.contrib.auth.models import Group
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django import forms

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm
from .models import SeatsModel


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
                try:
                    group = Group.objects.get(name=user.student_id[:3])
                except Group.DoesNotExist:
                    group = Group(name=user.student_id[:3]).save()
                user.groups.add(group)
                user.save()
                messages.success(request, '회원가입되었습니다.')
            except forms.ValidationError as e:
                messages.error(request, e)
        else:
            messages.error(request, form.errors)
        return redirect('index')


class SeatsView(View):
    def get(self, request):
        user = request.user

        if user.is_anonymous:
            return redirect('/')

        class_id = user.student_id[:3]
        seats, _ = SeatsModel.objects.get_or_create(class_id=class_id)

        return render(request, 'app/seats.html', {'seats': seats.get_seats()})
