from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _

SIZE_TYPES = (
    (0, _('Одежда')),
    (1, _('Головные уборы')),
    (2, _('Обувь'))
)

GEN_TYPES = (
    (0, _('Женский')),
    (1, _('Мужской')),
)

GLOBAL_SIZES = (
    ('XXS', _('XXS')),
    ('XS', _('XS')),
    ('S', _('S')),
    ('M', _('M')),
    ('L', _('L')),
    ('XL', _('XL')),
    ('XXL', _('XXL')),
    ('XXXL', _('XXXL')),
)

class Size(AbstractModel):
    size = models.PositiveIntegerField(_('Размер'), default=38, null=False, blank=True)
    size_global = models.CharField(_('Международное обозначение'), choices=GLOBAL_SIZES, max_length=6, null=True, blank=True)
    bust = models.PositiveIntegerField(_('Обхват груди, см'), null=True, blank=True)
    waist = models.PositiveIntegerField(_('Обхват талии, см'), null=True, blank=True)
    hips = models.PositiveIntegerField(_('Обхват бедер, см'), null=True, blank=True)
    gender = models.PositiveIntegerField(_('Пол'), choices=GEN_TYPES, null=False, blank=True)
    type = models.PositiveIntegerField(_('Тип размера'), choices=SIZE_TYPES, null=False, blank=True, default=0)
    
    def __str__(self):
        if(self.size_global == None):
            return f"{self.size} ({SIZE_TYPES[self.type][1]})" 
        return f"{self.size}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
      