# Generated by Django 4.0.3 on 2022-04-30 13:25

from django.db import migrations, models
import shop.models.image


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_alter_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_thumb',
            field=models.ImageField(blank=True, upload_to=shop.models.image.course_dir, verbose_name='Фото (50%)'),
        ),
    ]