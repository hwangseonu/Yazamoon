from django.forms import ModelForm, Form
from django import forms
from .models import UserModel, VerifyCode, UserManager


class LoginForm(Form):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class RegisterForm(ModelForm):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )
    verify_code = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Verify Code'})
    )

    class Meta:
        model = UserModel
        fields = ['email', 'password']

    def confirm(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])

        VerifyCode.objects.filter(code=self.cleaned_data['verify_code'])

        if commit:
            user.save()
        return user
