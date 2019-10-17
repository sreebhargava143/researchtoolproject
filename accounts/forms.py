from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms.widgets import PasswordInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username',
        validators=[MinLengthValidator(6), MaxLengthValidator(30)], required=True)
    email = forms.EmailField(label='Email', max_length=30, required=True)
    password = forms.CharField(label='Password',
        min_length=8, max_length=30, widget=PasswordInput, required=True)
    password2 = forms.CharField(label='Repeat Password', widget=PasswordInput, required=True)
