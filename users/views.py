# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,loader,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

import requests
import json

# Create your views here.


def index(request):
	return HttpResponse('Users module')

def profile(request):
	jsonList = []
	template = loader.get_template('users/profile.html')
	req = requests.get('https://api.github.com/users/alexconrey')
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
	  userData['name'] = data['name']
          userData['blog'] = data['blog']
          userData['email'] = data['email']
          userData['public_gists'] = data['public_gists']
          userData['public_repos'] = data['public_repos']
          userData['avatar_url'] = data['avatar_url']
          userData['followers'] = data['followers']
          userData['following'] = data['following']

        return HttpResponse(render(request, 'users/profile.html', context=userData))


def register(request):
	if request.method == 'POST':	
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return HttpResponse(render(request, 'users/register.html', context={'form': form}))
