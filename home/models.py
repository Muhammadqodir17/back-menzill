from django.db import models
from core.base import BaseModel



class Title(BaseModel):
    name = models.CharField(max_length=250)
    name2 = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Header(BaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    bg_image = models.ImageField(upload_to="header", blank=True)

    def __str__(self):
        return f'{self.title}'
    

class Partners(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to="partners/", blank=True)

    def __str__(self):
        return f'{self.title.name}'



class SocialMedia(BaseModel):
    name = models.CharField(max_length=250)
    link = models.URLField()
    image = models.ImageField(upload_to="social", blank=True)

    def __str__(self):
        return f'{self.link}'

