from django.urls import path
from .views import AboutViewSet, PrincipleViewSet

urlpatterns = [
    path('', AboutViewSet.as_view({'get': 'list'}), name='about'),
    path('principles/', PrincipleViewSet.as_view({'get': 'list'}), name='principle'),
]
