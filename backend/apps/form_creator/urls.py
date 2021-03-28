from django.urls import path, include
from rest_framework import routers
from .views import FormCreatorViewSet

from rest_framework.urlpatterns import format_suffix_patterns

# FormCreator API
# router = routers.DefaultRouter()
# router.trailing_slash = '/?'
#
# router.register(r'form/<str:pk>/', FormCreatorViewSet.as_view())

urlpatterns = [
    path('form/', FormCreatorViewSet.as_view()),
    path('form/<str:pk>/', FormCreatorViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
