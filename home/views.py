from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from .serializers import HeaderSerializer
from .models import Header
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class HomeViewSet(ViewSet):
    @swagger_auto_schema(
        responses={
            200: openapi.Response('All headers', HeaderSerializer(many=True)),
            404: 'Not found'
        },
        operation_description="Get all header objects",
        operation_summary="List all headers"
    )
    def header(self, request, *args, **kwargs):
        headers = Header.objects.all()
        serializer = HeaderSerializer(headers, many=True)
        return Response(serializer.data)