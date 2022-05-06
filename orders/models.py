from config.common_model import AbstractModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.color import Color
from shop.models.product import Product, ProductAvailability
from django.db.models.signals import post_init, post_save
from django.utils import timezone

from shop.models.size import Size


class Order(AbstractModel):
    user_name = models.CharField(_("Имя заказчика"), max_length=255)
    phone_num = models.CharField(_("Номер телефона"), max_length=16)
    done = models.BooleanField(_("Заказ выполнен"), default=False)
    total_price = models.PositiveIntegerField(null=False)

    def __str__(self):
        local_date = timezone.localtime(self.created_at, timezone.get_fixed_timezone(360)).date()
        local_time = timezone.localtime(self.created_at, timezone.get_fixed_timezone(360)).time()
        
        return f"Заказ: {self.user_name} - {self.phone_num} ({local_date} {local_time})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
      

class ProductOrder(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Товар"), blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name=_("Размер"), blank=True, default=1)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name=_("Цвет"), blank=True, default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products', verbose_name=_("Товар"), blank=True, null=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}-{self.size.size} ({self.color.name}); количество - {self.count}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'