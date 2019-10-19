from django.urls import path
from . import views

urlpatterns = [
    path("", views.explore, name="explore"),
    path("hotfeeds/", views.explorer_hot_feeds, name="explorer_hot_feeds"),
    path("topfeeds/", views.explorer_top_feeds, name="explorer_top_feeds"),
    path("risingfeeds/", views.explorer_rising_feeds, name="explorer_rising_feeds"),
    path("controversialfeeds/", views.explorer_controversial_feeds, name="explorer_controversial_feeds"),
    path("newfeeds/", views.explorer_new_feeds, name="explorer_new_feeds"),
]
