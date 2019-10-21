from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_username/', views.edit_username, name='edit_username'),
    path('profile/username_edit/', views.username_edit, name='username_edit'),
    path('profile/upload_photo/', views.upload_photo, name="upload_photo"),
    path('profile/photo_upload/', views.photo_upload, name="photo_upload"),
    path('profile/edit_email/', views.edit_email, name="edit_email"),
    path('profile/email_edit/', views.email_edit, name='email_edit'),

    path('bookmarks/', views.bookmarks, name='bookmarks'),
]
