from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import praw
from main.models import Story, StoryCard
from bookmarks.models import Bookmark
from main.forms import CardForm
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
    current_user = request.user
    bookmarks = Bookmark.objects.filter(user_id=current_user.id).all().values('id', 'bookmark_name')
    if request.method == 'POST':
        form = CardForm(request.POST, request=request)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
    else:
        form = CardForm(request=request)
    return render(request, 'create_story.html', {'form': form, 'story_id':story_id, 'story_name':story_name, 'description':description, 'bookmarks':bookmarks})
