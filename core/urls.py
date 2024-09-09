from .views import UserViewSet, activate
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('activate',activate)
    ] + router.urls
