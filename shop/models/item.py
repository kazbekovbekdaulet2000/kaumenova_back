from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from shop.models.color import Color
from shop.models.product_type import ProductType
from shop.models.size import Size
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from news.models import Collection
from django.core.validators import MaxValueValidator, MinValueValidator


PROD_TYPES = (
    (0, _('Чапан')),
    (1, _('Камзол')),
    (2, _('Желет')),
    (3, _('Головные уборы')),
)

class Product(AbstractModel):
    articule = models.CharField(_('Артикул'), max_length=255, null=False, blank=True)
    name = models.CharField(_('Название продукта'), max_length=255, null=False, blank=True)
    # description = RichTextField(verbose_name=_('Описание продукта'), config_name='basic')
    description = models.TextField(verbose_name=_('Описание продукта'), max_length=4096, null=True, blank=True)
    composition = models.TextField(verbose_name=_('Состав продукта'), max_length=4096, null=True, blank=True)
    model_size = models.PositiveIntegerField(verbose_name=_('Размер модели'), default=36, null=True)
    model_height = models.PositiveIntegerField(verbose_name=_('Рост модели'), default=170, null=True)
    price = models.PositiveIntegerField(_('Цена'), default=100000, null=False, blank=True)
    type = models.ForeignKey(ProductType, blank=True,on_delete=models.DO_NOTHING, verbose_name=_('Категория товара'), null=True)
    collection = models.ForeignKey(Collection, blank=True,on_delete=models.DO_NOTHING, verbose_name=_('Коллекция'), null=True)
    set_sizes = models.ManyToManyField(Size, blank=True)
    set_colors = models.ManyToManyField(Color, blank=True)
    discount = models.PositiveIntegerField(verbose_name=_('Скидка в процентах'), default=0, validators=[MaxValueValidator(100)])


    def __str__(self): 
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductAvailability(AbstractModel):
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING, verbose_name=_('Продукт'))
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, verbose_name=_('Размер'))
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, verbose_name=_('Цвет'))
    count = models.PositiveIntegerField(null=False)

    def __str__(self): 
        return f"{self.product.name}-{self.size.size} ({self.color.name})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Размер продукта'
        verbose_name_plural = 'Размеры продукта'



def update_product(sender, instance, created, **kwargs):
    product = instance.product
    product.set_sizes.add(instance.size)
    product.set_colors.add(instance.color)
    product.save()

post_save.connect(update_product, sender=ProductAvailability)
