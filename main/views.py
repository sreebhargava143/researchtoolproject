from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import praw
# Create your views here.


def home(request):
    context = {
        "page":"dashboard",
        }
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', context=context)
    return render(request, 'home.html')

@login_required
def dashboard(request):
    context = {
        "page":"dashboard",
    }
    return render(request, 'dashboard.html', context=context)

@login_required
def profile(request):
    return render(request, 'profile.html')

