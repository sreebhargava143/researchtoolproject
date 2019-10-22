from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from main.models import Story, StoryCard

# Create your views here.
@login_required
def story_list(request):
    current_user = request.user
    stories_list = Story.objects.filter(author=current_user).all().values('story_name', 'publish', 'description')
    return render(request, 'list_stories.html', {'stories_list': stories_list})

@login_required
def story_detail(request):
    current_user = request.user
    return render(request, 'story_detail.html')
