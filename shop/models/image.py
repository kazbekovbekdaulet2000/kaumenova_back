import os
import sys
from django.db import models
from config.common_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from shop.models.color import Color
from shop.models.product import Product
from PIL import Image as Picture
from django.core.files.uploadedfile import InMemoryUploadedFile


def course_dir(instance, filename):
    return f"product/product_{instance.product.id}/{filename}"


def thumbnail_folder(instance, filename):
    return f"thumbs/product_{instance.product.id}/{filename}"


class Image(AbstractModel):
    image = models.ImageField(verbose_name=_(
        'Фото'), null=False, blank=True, upload_to=course_dir)
    image_thumb = models.ImageField(
        upload_to=thumbnail_folder, max_length=500, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='images',
                                blank=True, on_delete=models.CASCADE, verbose_name=_('Продукт'))
    color = models.ForeignKey(
        Color, blank=True, on_delete=models.CASCADE, verbose_name=_('Цвет в фото'))

    def __str__(self):
        return f"{self.product.name} ({self.color.name})"

    def create_thumbnail(self):
        if not self.image:
            return

        from PIL import Image as Picture
        from io import BytesIO
        data_img = BytesIO()

        img = Picture.open(self.image)
        THUMBNAIL_SIZE = (int(img.width/1.75), int(img.height/1.75))

        img.thumbnail(THUMBNAIL_SIZE, Picture.ANTIALIAS)
        img.save(data_img, format='jpeg', quality=100)

        self.image_thumb = InMemoryUploadedFile(data_img,
                                                'ImageField',
                                                '%s_thumbnail.%s' % (os.path.splitext(
                                                    self.image.name)[0], 'jpeg'),
                                                'jpeg',
                                                sys.getsizeof(data_img), None)

    def save(self, *args, **kwargs):
        self.create_thumbnail()
        force_update = False
        if self.id:
            force_update = True
        super(Image, self).save(force_update=force_update)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
