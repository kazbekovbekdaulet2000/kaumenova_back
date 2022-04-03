from config.common_model import AbstractModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.item import ProductAvailability
from django.db.models.signals import post_init, post_save


class ProductOrder(AbstractModel):
    product = models.ForeignKey(ProductAvailability, on_delete=models.DO_NOTHING, verbose_name=_("Товар"), blank=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.product.name}-{self.product.size.size_global} ({self.product.color.name}); количество - {self.count}"


class Order(AbstractModel):
    user_name = models.CharField(_("Имя заказчика"), max_length=255)
    phone_num = models.CharField(_("Номер телефона"), max_length=16)
    done = models.BooleanField(_("Заказ выполнен"), default=False)
    products = models.ManyToManyField(ProductOrder, verbose_name=_("Товары"), blank=True)
    total_price = models.PositiveIntegerField(null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
      

# def init_order(sender, instance, created, **kwargs):
#     products = instance.product
#     print(products)
#     pass


# def update_product_counts(sender, instance, created, **kwargs):
#     products = instance.product
#     print(products)
#     pass

# post_init.connect(init_order, sender=Order)
# post_save.connect(update_product_counts)
