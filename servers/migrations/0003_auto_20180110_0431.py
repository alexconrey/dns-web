# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20180110_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='ctime',
        ),
        migrations.AddField(
            model_name='server',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]