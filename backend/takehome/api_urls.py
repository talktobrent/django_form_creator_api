
from django.urls import include, path
from rest_framework import routers

#from apps.form_creator.urls import router as form_router

from apps.form_creator.urls import urlpatterns



# router = routers.DefaultRouter()
# router.registry.extend(form_router.registry)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
