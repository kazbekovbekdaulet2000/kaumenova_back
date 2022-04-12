from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Color(AbstractModel):
    name = models.CharField(_('Название цвета'), max_length=255, null=False, blank=True)
    color = ColorField(default='#FF0000', null=False)
    color_code = models.PositiveIntegerField(_("Номер"), null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
