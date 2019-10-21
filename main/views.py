from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
import praw
from .forms import ProfileImageForm, EditUsernameForm
from .models import Profile
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
    username = request.user.username
    user = User.objects.get(username=username)
    image = user.profile.profile_image
    return render(request, 'profile.html', {'profile': 1, 'image': image})


@login_required
def upload_photo(request):
    username = request.user.username
    user = User.objects.get(username=username)
    image = user.profile.profile_image
    image_form = ProfileImageForm()
    return render(request, 'profile.html', {'profile': 1, 'image': image, 'image_form': image_form})


@login_required
def photo_upload(request):
    username = request.user.username
    user = User.objects.get(username=username)
    if request.method == "POST":
        print("YESS")
        image_form = ProfileImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            print("is VALID")
            image = image_form.cleaned_data.get('image')
            Profile.objects.update_or_create(user=user, defaults={'profile_image':image})
    return redirect('profile')


@login_required
def edit_username(request):
    username = request.user.username
    user = User.objects.get(username=username)
    image = user.profile.profile_image
    return render(request, 'profile.html', {'profile': 1, 'image': image, 'user_form': 1})


@login_required
def post_new_username(request):
    username = request.user.username
    user = User.objects.get(username=username)
    image = user.profile.profile_image
    if request.method == "POST":
        new_username = request.POST['username']
        user.username = new_username
        user.save()
        return redirect('profile')
    return redirect('profile')


