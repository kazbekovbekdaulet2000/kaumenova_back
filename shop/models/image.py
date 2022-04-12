from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from shop.models.color import Color
from shop.models.product import Product

def course_dir(instance, filename):
    return f"product/product_{instance.product.id}/{filename}"

class Image(AbstractModel):
    image = models.ImageField(verbose_name = _('Фото'), null=False, blank=True, upload_to=course_dir)
    product = models.ForeignKey(Product, related_name='images', blank=True, on_delete=models.CASCADE, verbose_name=_('Продукт'))
    color = models.ForeignKey(Color, blank=True, on_delete=models.CASCADE, verbose_name=_('Цвет в фото'))
    
    def __str__(self):
        return f"{self.product.name} ({self.color.name})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
      