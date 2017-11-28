# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Domain, RecordType, Record, Nameserver

class DomainAdmin(admin.ModelAdmin):
	model = Domain
	list_display = ['name', 'owner', ]

admin.site.register(Domain, DomainAdmin)
admin.site.register(RecordType)
admin.site.register(Record)
admin.site.register(Nameserver)

# Register your models here.

