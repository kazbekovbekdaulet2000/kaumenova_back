from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


def collection_dir(instance, filename):
    return f"collection_{instance.id}/{filename}"


class Collection(AbstractModel):
    name = models.CharField(max_length=4096, null=False, blank=True)
    image = models.ImageField(verbose_name=_(
        'Главное фото'), null=False, blank=True, upload_to=collection_dir)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Broadcast(AbstractModel):
    username = models.CharField(max_length=4096, null=False, blank=True)
    phone_number = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=16, null=True)

    def __str__(self):
        return f"{self.username} ({self.phone_number})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Люди подписавшие на новости'
        verbose_name_plural = 'Люди подписавшие на новости'


class News(AbstractModel):
    name = models.CharField(max_length=4096, null=False, blank=True)
    image = models.ImageField(verbose_name=_(
        'Фото'), null=False, blank=True, upload_to="news")
    active = models.BooleanField(default=True)
    text = RichTextField(verbose_name=_(
        'Тест новости'), config_name='basic')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
