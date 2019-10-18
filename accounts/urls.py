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
    
    # path('password_change/', auth.views.PasswordChangeView.as_view(), name="password_change"),
    
    # path('password_change/done', auth.views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
]
