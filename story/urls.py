from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('<int:id>/<str:story>', views.story_detail, name='story_detail'),
    path('storylines/<int:pk>', csrf_exempt(views.StorylineDetailViewSet.as_view()), name="storylines" ),
]
