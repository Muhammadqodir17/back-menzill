from rest_framework import serializers
from gallery.models import GalleryModel
from home.models import Title


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = ['id', 'image']
        read_only_fields = ['id']


class TitleGallerySerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'name', 'name2', 'gallery']
