import os
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
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


def product_dir(instance, filename):
    return f"product/product_{instance.product.id}/{filename}"


def thumb_dir(instance, filename):
    return f"product/product_{instance.product.id}/thumbs/{filename}"


class News(AbstractModel):
    name = models.CharField(max_length=4096, null=False, blank=True)
    image = models.ImageField(verbose_name=_('Фото'), null=False, blank=True, upload_to="news")
    video = models.FileField(verbose_name=_('Видео'), null=True, blank=True)
    image_thumb240 = models.ImageField(verbose_name=_('Фото (240px)'), upload_to='news/thumbs', max_length=500, null=True, blank=True)
    image_thumb480 = models.ImageField(verbose_name=_('Фото (480px)'), upload_to='news/thumbs', max_length=500, null=True, blank=True)
    image_thumb720 = models.ImageField(verbose_name=_('Фото (720px)'), upload_to='news/thumbs', max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    text = RichTextField(verbose_name=_('Тест новости'), config_name='basic')

    def __str__(self):
        return self.name
   
    def create_thumbnail(self, newsize) -> InMemoryUploadedFile:
        if not self.image:
            return
        data_img = BytesIO()

        img = Image.open(self.image)
        img = img.convert('RGB')
        if(img.height/newsize <= 1 or img.width/newsize <= 1):
            return None

        if(img.width > img.height):
            width = int(newsize)
            height = int(img.height/(img.width/newsize))
        else:
            height = int(newsize)
            width = int(img.width/(img.height/newsize))

        THUMBNAIL_SIZE = (width, height)
        img.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        img.save(data_img, format='jpeg', quality=100)

        return InMemoryUploadedFile(data_img,
                                    'ImageField',
                                    '%s_thumbnail_%spx.%s' % (os.path.splitext(
                                        self.image.name)[0], int(newsize), 'jpeg'),
                                    'jpeg',
                                    sys.getsizeof(data_img), None)

    def save(self, *args, **kwargs):
        if(not self.image_thumb240):
            self.image_thumb240 = self.create_thumbnail(240)
        if(not self.image_thumb480):
            self.image_thumb480 = self.create_thumbnail(480)
        if(not self.image_thumb720):
            self.image_thumb720 = self.create_thumbnail(720)

        force_update = False
        if self.id:
            force_update = True
        super(News, self).save(force_update=force_update, *args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
