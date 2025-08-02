from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base import BaseModel
from home.models import Title


class GalleryModel(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        db_table = 'gallery'

    def __str__(self):
        return self.id
