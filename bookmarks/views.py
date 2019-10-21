from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkViewSet(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    def get_queryset(self):
        user = self.request.user.id
        return Bookmark.objects.filter(user_id=user).all()

class BookmarkDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

