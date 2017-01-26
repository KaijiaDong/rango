# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 15:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170126_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 1, 26, 15, 42, 9, 247249, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
