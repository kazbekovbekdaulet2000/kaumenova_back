# Generated by Django 4.0.3 on 2022-05-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_producttype_options_producttype_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productavailability',
            name='count',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
