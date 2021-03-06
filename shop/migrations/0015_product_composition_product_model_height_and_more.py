# Generated by Django 4.0.3 on 2022-04-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_articule_producttype_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.TextField(max_length=4096, null=True, verbose_name='Состав продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='model_height',
            field=models.PositiveIntegerField(default=36, null=True, verbose_name='Рост модели'),
        ),
        migrations.AddField(
            model_name='product',
            name='model_size',
            field=models.PositiveIntegerField(default=36, null=True, verbose_name='Размер модели'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=4096, null=True, verbose_name='Описание продукта'),
        ),
        migrations.CreateModel(
            name='ProductsCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='shop.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
