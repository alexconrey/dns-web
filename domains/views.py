# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render, HttpResponse
from .models import Domain



# Create your views here.

def index(request):
	return HttpResponse(render(request, 'domains/base.html', context={}))

def list_domains(request):
	domains = Domain.objects.filter(owner=request.user).values()

	return HttpResponse(render(request, 'domains/list_domains.html', context={'domains': domains}))	

