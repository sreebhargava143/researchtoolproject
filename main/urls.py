from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('home/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_username/', views.edit_username, name='edit_username'),
    path('profile/username_edit/', views.post_new_username, name='post_new_username'),
    path('profile/upload_photo/', views.upload_photo, name="upload_photo"),
    path('profile/photo_upload/', views.photo_upload, name="photo_upload"),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
]
