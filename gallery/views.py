from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class GalleryViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="Get title",
        operation_summary="Get Title",
        responses={200: GalleryTitleSerializer()},
        tags=['gallery']
    )
    def get_title(self, request, *args, **kwargs):
        titles = GalleryTitle.objects.all().first()
        if not titles:
            return Response({"error": "GalleryTitle not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = GalleryTitleSerializer(titles, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



    @swagger_auto_schema(
        operation_description="Get All Galleries",
        operation_summary="Get Galleries",
        responses={200: GallerySerializer(many=True)},
        tags=['gallery']
    )
    def get_gallery(self, request, *args, **kwargs):
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(galleries, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)