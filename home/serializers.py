from rest_framework import serializers
from catalog.models import Catalog, Material, Product
from .models import Header


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'title', 'description', 'bg_image']


class NestedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image']


class GetProductsSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    title2 = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'title2', 'products']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['title'] = instance.title.name
        return data

    def get_products(self, obj):
        request = self.context.get('request')
        products = Product.objects.filter(catalog=obj.catalog)
        return NestedProductSerializer(products, many=True, context={'request': request}).data

    def get_title2(self, obj):
        return obj.title.name2


class NestedMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'description', 'image']


class GetMaterialsSerializer(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'materials']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['title'] = instance.title.name
        return data

    def get_materials(self, obj):
        request = self.context.get('request')
        materials = Material.objects.filter(catalog=obj.catalog)
        return NestedProductSerializer(materials, many=True, context={'request': request}).data