# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20170415_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.WhiteBoardUser'),
            preserve_default=False,
        ),
    ]
