# Generated by Django 4.0.3 on 2022-04-03 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_alter_news_image'),
        ('shop', '0012_alter_productavailability_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='news.collection', verbose_name='Коллекция'),
        ),
    ]