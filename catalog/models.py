from django.db import models
from home.models import Title
from core.base import BaseModel


class Catalog(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class Material(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='material/', blank=True)

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=Title)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='product/', blank=Title)

    def __str__(self):
        return f'{self.name}'


