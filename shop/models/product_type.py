from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


PROD_TYPES = (
    (0, _('Чапан')),
    (1, _('Камзол')),
    (2, _('Желет')),
    (3, _('Головные уборы')),
)


class ProductType(AbstractModel):
    name = models.CharField(_('Название категории'),max_length=255, null=False, blank=True)
    order = models.PositiveIntegerField(_('Очередь'), default=1)
    year = models.PositiveIntegerField(_('Год'), default=2021, validators=[MaxValueValidator(2050), MinValueValidator(1991)])
    have_size = models.BooleanField(_('Есть размеры'), default=True)

    def __str__(self):
        return f"{self.name} {self.year}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории продуктов'
