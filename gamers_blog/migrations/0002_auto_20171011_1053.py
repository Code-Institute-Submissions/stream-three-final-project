# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_slug',
            field=models.SlugField(max_length=250, unique_for_date='published_date'),
        ),
    ]
