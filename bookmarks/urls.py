from django.urls import include, path
from bookmarks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.BookmarkViewSet.as_view(), name='bookmarks'),
    path('<int:pk>/', views.BookmarkDetailViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns = format_suffix_patterns(urlpatterns)