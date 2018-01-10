# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from .models import Domain, Record
from .forms import DomainForm, RecordForm



# Create your views here.

def index(request):
	return HttpResponse(render(request, 'domains/base.html', context={}))

def list_domains(request):
	domains = Domain.objects.filter(owner=request.user).values()

	return HttpResponse(render(request, 'domains/list_domains.html', context={'domains': domains}))	

def list_records(request):
    records = Record.objects.values()

    return HttpResponse(render(request, 'domains/list_records.html', context={'records': records}))

def create_domain(request):
        if request.method == 'POST':
            domain = Domain()
            form = DomainForm(request.POST, instance=domain)
            if form.is_valid():
                if not Domain.objects.filter(name = form.cleaned_data['name'])[0]:
                    domain.save()
                return redirect('/domains/list')
        else:
            form = DomainForm()
        return HttpResponse(render(request, 'domains/create.html', {'form': form}))

def create_record(request):
    if request.method == 'POST':
        record = Record()
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            if not Record.objects.filter(domain = form.cleaned_data['domain']).filter(name = form.cleaned_data['name']):
                record.save()
            return redirect('/domains/records/list')
    else:
        form = RecordForm()
    return HttpResponse(render(request, 'domains/create.html', {'form': form}))
