from django.urls import path
from . import views

urlpatterns = [
# path('search/', views.search_reddit, name='search'),
path('subreddit/', views.search_reddit, name='search'),
path('comments/<str:sub_name>/', views.comments, name='comments'),
]