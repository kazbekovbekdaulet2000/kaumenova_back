# Generated by Django 4.0.3 on 2022-05-11 07:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_alter_image_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), blank=True, null=True, size=None),
        ),
    ]
