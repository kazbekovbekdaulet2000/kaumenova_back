# Generated by Django 4.0.3 on 2022-04-02 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_producttype_product_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'ordering': ['-created_at'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории продуктов'},
        ),
        migrations.RenameField(
            model_name='size',
            old_name='type',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название категории'),
        ),
    ]
