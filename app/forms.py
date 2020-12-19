from django.forms import ModelForm
from django import forms
from .models import UserModel, VerifyCode


class LoginForm(ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = UserModel
        fields = ['username', 'password']


class RegisterForm(ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    verify_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Verify Code'}))

    class Meta:
        model = UserModel
        fields = ['username', 'password']

    def save(self, commit=True):
        VerifyCode.objects.filter(code=self.cleaned_data['verify_code'])

