# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20170415_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('stream', models.CharField(max_length=255)),
                ('submission_date', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='whiteboarduser',
            name='stream',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
