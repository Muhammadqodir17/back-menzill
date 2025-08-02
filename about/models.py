from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base import BaseModel
from home.models import Title


class AboutModel(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='about', verbose_name=_('Related Title'))
    name = models.CharField(max_length=100, verbose_name=_("Name"), help_text=_("Enter the name for the About"))
    description = models.TextField(verbose_name=_("Description"), help_text=_("Enter the description for the About"))
    image_1 = models.ImageField(upload_to='about/', verbose_name=_("Image"),
                                help_text=_("Upload an image 1 for the About"), )
    image_2 = models.ImageField(upload_to='about/', verbose_name=_("Image"),
                                help_text=_("Upload an image 2 for the About"), )

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        db_table = "about"

    def __str__(self):
        return self.name


class PrincipleModel(BaseModel):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='principle',
                              verbose_name=_('Related Title'))
    name = models.CharField(max_length=100, verbose_name=_('Name'), help_text=_('Enter the name for the Principle'))
    description = models.TextField(verbose_name=_('Description'), help_text=_('Enter principle description text'))
    icon = models.ImageField(upload_to='principle/', verbose_name=_('Icon'),
                             help_text=_('Upload an icon for the Principle'))

    class Meta:
        verbose_name = _('Principle')
        verbose_name_plural = _('Principles')
        db_table = 'principle'

    def __str__(self):
        return self.name
