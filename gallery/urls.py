from django.urls import path
from .views import GalleryViewSet

urlpatterns = [
    path('get_gallery_title/', GalleryViewSet.as_view({'get': 'get_title'}), name='get_gallery_title'),
    path('get_gallery/', GalleryViewSet.as_view({'get': 'get_gallery'}), name='get_gallery'),
]

