from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from .forms import LoginForm, RegisterForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {
            'login': LoginForm(prefix='login'),
            'register': RegisterForm(prefix='register')
        })


class LoginView(View):
    def post(self, request: HttpRequest):
        pass


class RegisterView(View):
    def post(self, request: HttpRequest):
        pass
