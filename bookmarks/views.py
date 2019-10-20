from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkViewSet(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

