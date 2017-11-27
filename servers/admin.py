# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Server,Region

admin.site.register(Server)
admin.site.register(Region)

# Register your models here.
