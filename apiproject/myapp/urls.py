from django.urls import path
from django.urls.conf import include
from myapp import views
from myapp.views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls))
]
