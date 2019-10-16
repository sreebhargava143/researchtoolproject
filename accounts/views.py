from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import SignUpForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        print('post request')
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('form is valid')
            if form.cleaned_data.get('password') == form.cleaned_data.get('password2'):
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = User(username=username, email=email, password=password)
                user.save()
    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form})
