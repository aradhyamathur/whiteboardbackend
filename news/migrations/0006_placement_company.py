# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170401_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='company',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
