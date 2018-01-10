# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Server
from .forms import ServerForm

# Create your views here.


def index(request):
	return HttpResponse('Hello World!')

def list_servers(request):
    server_list = []
    for server in Server.objects.values():
        server_list.append(server)

    return HttpResponse(render(request, 'servers/list_servers.html', {'servers': server_list}))

def list_regions(request):
    return HttpResponse(render(request, 'servers/list_regions.html'))

def create_server(request):
        if request.method == 'POST':
            server = Server()
            form = ServerForm(request.POST, instance=server)
            if form.is_valid():
                server.save()
                return redirect('/servers/list')
        else:
            form = ServerForm()
        return HttpResponse(render(request, 'servers/create.html', {'form': form}))

