# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamersblog', '0006_blogpost_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_tags',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
