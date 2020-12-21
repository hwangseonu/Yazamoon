from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm


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
                return redirect('index')
            else:
                messages.error(request,  '아이디나 비밀번호가 일치하지 않습니다.')
                return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('index')


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect('index')


class RegisterView(View):
    def post(self, request: HttpRequest):
        pass
