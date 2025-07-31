from rest_framework import serializers
from models import *
from home.models import Title


class GalleryTitleSerializer(serializers.ModelSerializer):
    main_title = serializers.SerializerMethodField()
    main_title_id = serializers.PrimaryKeyRelatedField(queryset=Title.objects.all(), source='main_title', write_only=True)

    class Meta:
        model = GalleryTitle
        fields = ['id', 'main_title', 'main_title_id', 'title']

    def get_main_title(self, obj):
        return obj.main_title.name




class GallerySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title', read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'description', 'image']




class GalleriesSerializer(serializers.ModelSerializer):
    galleries = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = GalleryTitle
        fields = ['id', 'title', 'galleries']
