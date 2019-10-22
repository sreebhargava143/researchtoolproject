from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from main.models import Story, StoryCard
from .models import Storyline
from .serializers import StorylineSerializer
from rest_framework import viewsets, generics

# Create your views here.
@login_required
def story_list(request):
    current_user = request.user
    stories_list = Story.objects.filter(author=current_user).all().values('id', 'story_name', 'publish', 'description')
    return render(request, 'list_stories.html', {'stories_list': stories_list})

@login_required
def story_detail(request, id, story):
    current_user = request.user
    return render(request, 'story_detail.html')

class StorylineDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StorylineSerializer
    def get_queryset(self):
        story_id = self.request.path_info.split('/').pop()
        return Storyline.objects.filter(story_id=story_id).all()