from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms.widgets import PasswordInput
from django import forms
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Field, Fieldset, ButtonHolder

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

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'register'
        self.helper.layout = Layout(
            Field('username', css_class='form-control',),
            Field('email', css_class="form-control"),
            Field('password', css_class="form-control"),
            Field('password2', css_class="form-control"),
            Submit('submit', 'Register')
        )
