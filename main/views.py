from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import praw
from main.models import Story
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return render(request, 'home.html')

@login_required
def dashboard(request):
    reddit = praw.Reddit(
        client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")

    feeds = reddit.subreddit('all').top(limit=1)
    context = {
        'feeds':feeds,
    }
    return render(request, 'dashboard.html', context=context)

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def bookmarks(request):
    return render(request, 'bookmarks.html')

@login_required
def create_story(request):
    if request.method == 'GET':
        if request.GET.get('story_name') and request.GET.get('description'):
            story = Story()
            story.story_name = request.GET.get('story_name')
            story.description = request.GET.get('description')
            story.author = request.user
            story.save()
    return render(request, 'create_story.html')

@login_required
def story_card(request):
    # if request.method == 'POST':
    #     if request.POST.get()
    return
