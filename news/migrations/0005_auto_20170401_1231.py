# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170401_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='image_field',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]