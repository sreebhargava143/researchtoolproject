from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import praw
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return render(request, 'home.html')

@login_required
def dashboard(request):
    # reddit = praw.Reddit(
    #     client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")

    # feeds = reddit.subreddit('all').top(limit=1)
    context = {
        'feeds':None,
    }
    return render(request, 'dashboard.html', context=context)

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def bookmarks(request):
    return render(request, 'bookmarks.html')
