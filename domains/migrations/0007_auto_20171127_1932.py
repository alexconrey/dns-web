# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0006_auto_20171127_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='domain',
            name='serial_number',
            field=models.IntegerField(default='2017112700'),
        ),
    ]
