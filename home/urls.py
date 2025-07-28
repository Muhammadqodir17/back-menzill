from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('get_header/', HomeViewSet.as_view({'get': 'header'}), name='home_header'),
    path('get_products/<int:pk>/', HomeViewSet.as_view({'get': 'get_products'}), name='home_products'),
    path('get_materials/<int:pk>/', HomeViewSet.as_view({'get': 'get_materials'}), name='home_materials'),
]