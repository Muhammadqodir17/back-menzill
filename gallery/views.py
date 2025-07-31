from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema


class GalleryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all Gallery Titles",
        operation_summary="Get Gallery Titles",
        responses={200: GalleryTitleSerializer(many=True)},
        tags=["gallery"]
    )
    def titles(self, request, *args, **kwargs):
        titles = GalleryTitle.objects.all()
        serializer = GalleryTitleSerializer(titles, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get one Gallery by ID",
        operation_summary="Get Single Gallery",
        responses={200: GallerySerializer()},
        tags=["gallery"]
    )
    def get_gallery(self, request, *args, **kwargs):
        gallery_id = kwargs.get('pk')
        gallery = Gallery.objects.filter(id=gallery_id).first()
        if not gallery:
            return Response({"error": "Gallery not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = GallerySerializer(gallery, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Galleries",
        operation_summary="Get Galleries by Title ID",
        responses={200: GalleriesSerializer()},
        tags=["gallery"]
    )
    def get_galleries(self, request, *args, **kwargs):
        title_id = kwargs.get('pk')
        title = GalleryTitle.objects.filter(id=title_id).first()
        if not title:
            return Response({"error": "GalleryTitle not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GalleriesSerializer(title, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


