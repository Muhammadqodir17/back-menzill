from rest_framework import serializers
from models import Gallery, GalleryTitle
from home.models import Title


class GalleryTitleSerializer(serializers.ModelSerializer):
    main_title = serializers.CharField(source='main_title.name', read_only=True)

    class Meta:
        model = GalleryTitle
        fields = ['id', 'main_title', 'title']


class GallerySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title', read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'description', 'image']
