# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_newsfeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='news_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
