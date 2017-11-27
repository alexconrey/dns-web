# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Domain, RecordType, Record

admin.site.register(Domain)
admin.site.register(RecordType)
admin.site.register(Record)

# Register your models here.

