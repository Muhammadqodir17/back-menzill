from django.contrib import admin
from .models import Catalog, Material, Product

admin.site.register(Catalog)
admin.site.register(Material)
admin.site.register(Product)