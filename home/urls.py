from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('header/', HomeViewSet.as_view({'get': 'header'}), name='home-header'),
]