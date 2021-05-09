from django.forms import forms
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .forms import LoginForm, RegisterForm


class LoginView(View):
    def post(self, request):
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
    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):
    def post(self, request):
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
