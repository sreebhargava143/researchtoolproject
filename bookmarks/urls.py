from django.urls import include, path
from bookmarks import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(views.BookmarkViewSet.as_view()), name='bookmarks'),
    path('<int:pk>/', csrf_exempt(views.BookmarkDetailViewSet.as_view())),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns = format_suffix_patterns(urlpatterns)


