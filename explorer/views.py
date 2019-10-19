from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@login_required
def explore(request):
    return render(request, 'explorer.html')
