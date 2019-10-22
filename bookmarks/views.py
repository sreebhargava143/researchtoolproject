from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Bookmark
from .serializers import BookmarkSerializer
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import JsonResponse

class BookmarkViewSet(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    def get_queryset(self):
        user = self.request.user.id
        return Bookmark.objects.filter(user_id=user).all()

class BookmarkDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

def get_bookmark_by_name(request, bookmark):
    if request.method == 'GET':
        user = request.user.id
        bookmark = Bookmark.objects.filter(user_id=user, bookmark_name=bookmark).first()
        if(bookmark):
            response = {
                'response': "true"
            }
        else:
            response = {
                'present': "false"
            }
    else:
        response = {
            'response':{
                'status':'FAILED',
                'ERROR':'METHOD NOT SUPPORTED'
            }
        }
    return JsonResponse(response)