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
                raise forms.ValidationError('패스워드가 일치하지 않습니다.')
            return password2

        if not VerifyCode.objects.filter(code=self.cleaned_data['verify_code']).exists():
            raise forms.ValidationError('유효하지 않은 인증코드입니다.')

    def save(self, commit=True):
        self.confirm()

        user = super(RegisterForm, self).save(commit=False)

        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])

        code = VerifyCode.objects.get(code=self.cleaned_data['verify_code'])
        user.student_id = code.student_id
        user.name = code.name

        code.delete()

        if commit:
            user.save()

        return user
