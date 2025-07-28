from django.db import models
from core.base import BaseModel


class Title(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

class Header(BaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    bg_image = models.ImageField(upload_to="header")