from django import forms


class ProfileImageForm(forms.Form):
    image = forms.ImageField()


class EditUsernameForm(forms.Form):
    username = forms.CharField(max_length=30)