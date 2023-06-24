from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from captcha.fields import CaptchaField

class CaptchaLoginForm(forms.Form):
    captcha = CaptchaField()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email']

class UserUpdatePassForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']