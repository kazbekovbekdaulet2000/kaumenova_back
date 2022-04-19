from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from shop.models.product import Product, ProductAvailability


class Card(AbstractModel):
    hash = models.CharField(max_length=255, default="0")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductAvailability, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
      