from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from home.models import Title
from .serializers import TitleAboutSerializer, TitlePrincipleSerializer


class AboutViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get About list",
        operation_description="Retrieve a list of all About data with related Title",
        responses={
            200: openapi.Response(
                description="About data successfully retrieved.",
                schema=TitleAboutSerializer(many=True)
            )
        },
        tags=['About']
    )
    def list(self, request):
        queryset = Title.objects.filter(
            about__isnull=False
        ).distinct().prefetch_related('about')

        serializer = TitleAboutSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PrincipleViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get Principles list",
        operation_description="Retrieve a list of all Principles data with related Title",
        responses={
            200: openapi.Response(
                description="Principles successfully retrieved.",
                schema=TitlePrincipleSerializer(many=True)
            )
        },
        tags=['Principles']
    )
    def list(self, request):
        queryset = Title.objects.filter(
            principle__isnull=False
        ).distinct().prefetch_related('principle')

        serializer = TitlePrincipleSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
