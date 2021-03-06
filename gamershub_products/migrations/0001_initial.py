# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamersHubProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_images', models.ImageField(blank=True, height_field='image_height', upload_to='gamershub/product_images/%d/%m/%Y', width_field='image_width')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Gamers Hub Products',
            },
        ),
    ]
