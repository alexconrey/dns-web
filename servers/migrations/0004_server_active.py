# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_remove_server_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='active',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2),
        ),
    ]