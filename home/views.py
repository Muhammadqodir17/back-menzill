from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from catalog.models import Catalog, Product, Material
from .serializers import HeaderSerializer, GetProductsSerializer, GetMaterialsSerializer
from .models import Header
from drf_yasg.utils import swagger_auto_schema


class HomeViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Header",
        operation_summary="Get Header",
        responses={
            200: HeaderSerializer(),
        },
        tags=['home']
    )
    def header(self, request, *args, **kwargs):
        headers = Header.objects.all()
        serializer = HeaderSerializer(headers, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Products By Catalog Id",
        operation_summary="Get Products By Catalog Id",
        responses={
            200: GetProductsSerializer(),
        },
        tags=['home']
    )
    def get_products(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()
        if catalog is None:
            return Response(data={'error': 'Catalog not found'}, status=status.HTTP_404_NOT_FOUND)
        products = Product.objects.filter(catalog=catalog).first()
        serializer = GetProductsSerializer(products, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Materials By Catalog Id",
        operation_summary="Get Materials By Catalog Id",
        responses={
            200: GetMaterialsSerializer(),
        },
        tags=['home']
    )
    def get_material(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()
        if catalog is None:
            return Response(data={'error': 'Catalog not found'}, status=status.HTTP_404_NOT_FOUND)
        materials = Material.objects.filter(catalog=catalog).first()
        serializer = GetMaterialsSerializer(materials, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)