from rest_framework import serializers
from .models import AboutModel, PrincipleModel
from home.models import Title


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ['id', 'name', 'description', 'image_1', 'image_2']
        read_only_fields = ['id']


class TitleAboutSerializer(serializers.ModelSerializer):
    about = AboutSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'name', 'name2', 'about']


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipleModel
        fields = ['id', 'name', 'description', 'icon']
        read_only_fields = ['id']


class TitlePrincipleSerializer(serializers.ModelSerializer):
    principle = PrincipleSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'name', 'name2', 'principle']
