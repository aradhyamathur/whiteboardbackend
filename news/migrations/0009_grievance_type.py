# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_newsfeed_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='type',
            field=models.CharField(default='Check', max_length=50),
        ),
    ]
