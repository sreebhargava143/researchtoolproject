from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('home/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
]
