from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.explore, name="explore"),
    path("hotfeeds/", views.explorer_hot_feeds, name="explorer_hot_feeds"),
    path("topfeeds/", views.explorer_top_feeds, name="explorer_top_feeds"),
    path("risingfeeds/", views.explorer_rising_feeds, name="explorer_rising_feeds"),
    path("controversialfeeds/", views.explorer_controversial_feeds, name="explorer_controversial_feeds"),
    path("newfeeds/", views.explorer_new_feeds, name="explorer_new_feeds"),
    path("search/" , login_required(views.explorer_search), name="explorer_search"),
    path("bookmarks/" , login_required(views.explorer_bookmarks), name="explorer_bookmarks"),
    
]
