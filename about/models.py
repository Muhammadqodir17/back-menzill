from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base import BaseModel
from home.models import Title


class AboutModel(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='about')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        db_table = "about"

    def __str__(self):
        return self.name


class PrincipleModel(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='principle')
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='principle/')

    class Meta:
        verbose_name = _('Principle')
        verbose_name_plural = _('Principles')
        db_table = 'principle'

    def __str__(self):
        return self.name
