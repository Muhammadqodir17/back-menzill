from django.db import models
from core.base import BaseModel


class Title(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'



