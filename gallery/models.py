from django.db import models
from home.models import Title
from core.base import BaseModel

class GalleryTitle(models.Model):
    main_title  = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.main_title} ({self.title})"


class Gallery(BaseModel):
    title = models.ForeignKey(GalleryTitle, on_delete=models.CASCADE, related_name='galleries')
    description = models.TextField()
    image = models.ImageField(upload_to="gallery", blank=True)

    def __str__(self):
        return f"{self.title.title}"
