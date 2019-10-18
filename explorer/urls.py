from django.urls import path
from . import views

urlpatterns = [
# path('search/', views.search_reddit, name='search'),
path('subreddit/', views.search_reddit, name='search'),
path('comments/', views.comments, name='comments'),
]