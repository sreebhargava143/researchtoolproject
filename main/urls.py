from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('home/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('create_story/', views.create_story, name='create_story'),
    path('story_card/<int:story_id>/<str:story_name>/<str:description>/', views.story_card, name='story_card'),
]
