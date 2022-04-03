from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _

PROD_TYPES = (
    (0, _('Чапан')),
    (1, _('Камзол')),
    (2, _('Желет')),
    (3, _('Головные уборы')),
)


class ProductType(AbstractModel):
    name = models.CharField(_('Название категории'),max_length=255, null=False, blank=True)
    have_size = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории продуктов'
