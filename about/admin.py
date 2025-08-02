from django.contrib import admin
from .models import AboutModel, PrincipleModel


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(PrincipleModel)
class PrincipleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)
    readonly_fields = ('created_at', 'updated_at')
