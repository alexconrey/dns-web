# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from .models import Domain
from .forms import DomainForm



# Create your views here.

def index(request):
	return HttpResponse(render(request, 'domains/base.html', context={}))

def list_domains(request):
	domains = Domain.objects.filter(owner=request.user).values()

	return HttpResponse(render(request, 'domains/list_domains.html', context={'domains': domains}))	

def create_domain(request):
    try:
        if request.method == 'POST':
            domain = Domain()
            form = DomainForm(request.POST, instance=domain)
            if form.is_valid():
                domain.save()
                return redirect('/domains/list')
        else:
            form = DomainForm()
        return HttpResponse(render(request, 'domains/create.html', {'form': form}))
    except Domain.MultipleObjectsReturned as duplicate_entry:
        return duplicate_entry
