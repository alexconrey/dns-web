# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_server_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='ctime',
            field=models.DateTimeField(),
        ),
    ]