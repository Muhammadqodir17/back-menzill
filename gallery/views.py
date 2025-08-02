from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from home.models import Title
from .serializers import TitleGallerySerializer


class GalleryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get Galleries list",
        operation_description="Retrieve a list of all Galleries data with related Title",
        responses={
            200: openapi.Response(
                description="Galleries successfully retrieved.",
                schema=TitleGallerySerializer(many=True)
            )
        },
        tags=['Galleries']
    )
    def list(self, request):
        queryset = Title.objects.filter(gallery__isnull=False).distinct().prefetch_related('gallery')

        serializer = TitleGallerySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
