# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamersblog', '0002_auto_20171030_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_title',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
