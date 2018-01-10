# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Server, Region
from .forms import ServerForm, RegionForm

# Create your views here.


def index(request):
	return HttpResponse('Hello World!')

def list_servers(request):
    server_list = []
    for server in Server.objects.values():
        server_list.append(server)

    return HttpResponse(render(request, 'servers/list_servers.html', {'servers': server_list}))

def list_regions(request):
    region_list = []
    for region in Region.objects.values():
        region_list.append(region)

    return HttpResponse(render(request, 'servers/list_regions.html', {'regions': region_list}))

def create_server(request):
        if request.method == 'POST':
            server = Server()
            form = ServerForm(request.POST, instance=server)
            if form.is_valid():
                if not Region.objects.filter(name = form.cleaned_data['name']):
                    server.save()
                return redirect('/servers/list')
        else:
            form = ServerForm()
        return HttpResponse(render(request, 'servers/create.html', {'form': form}))

def create_region(request):
        if request.method == 'POST':
            region = Region()
            form = RegionForm(request.POST, instance=region)
            if form.is_valid():
                if not Region.objects.filter(name = form.cleaned_data['name'])[0]:
                    region.save()
                return redirect('/servers/regions/list')
        else:
            form = RegionForm()
        return HttpResponse(render(request, 'servers/create_region.html', {'form': form}))
