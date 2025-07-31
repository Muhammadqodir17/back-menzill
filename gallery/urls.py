from django.urls import path
from .views import GalleryViewSet

urlpatterns = [
    path('get_titles/', GalleryViewSet.as_view({'get': 'titles'}), name='gallery_titles'),
    path('get_gallery/<int:pk>/', GalleryViewSet.as_view({'get': 'gallery'}), name='gallery'),
    path('get_galleries/<int:pk>/', GalleryViewSet.as_view({'get': 'get_galleries'}), name='galleries'),
]
