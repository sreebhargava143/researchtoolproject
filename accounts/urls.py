from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    # path('search/', views.search_reddit, name='search'),
    path('subreddit/', views.search_reddit, name='search'),
    path('comments/', views.comments, name='comments')
]
