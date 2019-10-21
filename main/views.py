from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import praw
from main.models import Story, StoryCard
from main.forms import CardForm
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
        story_name = request.GET.get('story_name')
        description = request.GET.get('description')
        if story_name and description:
            story = Story()
            story.story_name = story_name
            story.description = description
            story.author = request.user
            story.save()
            story_id = Story.objects.all().values('id').order_by('id').last()['id']
            return redirect('story_card', story_name=story_name, description=description, story_id=story_id)

@login_required
def story_card(request, story_id, story_name, description):
    
    if request.method == 'POST':
        form = CardForm(request.POST, request=request)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
    else:
        form = CardForm(request=request)
    return render(request, 'create_story.html', {'form': form, 'story_id':story_id, 'story_name':story_name, 'description':description})
