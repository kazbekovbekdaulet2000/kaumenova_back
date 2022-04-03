from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from shop.models.color import Color
from ckeditor.fields import RichTextField


class Cataloge(AbstractModel):
    name = models.CharField(_('Название продукта'), max_length=255, null=False, blank=True)
    description = RichTextField(verbose_name=_('Описание продукта'), config_name='basic')
    image = models.ImageField(verbose_name = _('Фото'), null=False, blank=True, upload_to="cataloge")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
      