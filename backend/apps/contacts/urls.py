from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, ContactViewSet

router = DefaultRouter()
router.register("tag", TagViewSet)
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = router.urls
