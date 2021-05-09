from django.shortcuts import render
from django.views import View

from user.forms import LoginForm, RegisterForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {
            'login': LoginForm(prefix='login'),
            'register': RegisterForm(prefix='register')
        })
