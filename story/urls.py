from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('<slug:story>/', views.story_detail, name='story_detail')
]
