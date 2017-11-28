# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 02:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domains', '0010_auto_20171128_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='owner',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='domain_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
