# Generated by Django 4.0.3 on 2022-04-03 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productavailability',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.product', verbose_name='Продукт'),
        ),
    ]
