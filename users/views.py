# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError

from django.shortcuts import render,HttpResponse,loader,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.forms.models import model_to_dict


from forms import RegisterForm, UserForm, ProfileForm

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from models import Profile

import requests
import json

# Create your views here.


def index(request):
	return HttpResponse('Users module')

@csrf_exempt
def profile(request):
	if request.method == 'POST':
		return update_profile(request)
	else:
		profile = model_to_dict(Profile.objects.get(pk=request.user.id))
		user = model_to_dict(User.objects.get(pk=request.user.id)) 
	
		return HttpResponse(render(request, 'users/profile.html', context={'profile': profile, 'user': user}))

@csrf_exempt
def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		try:
			print profile_form.data
			profile_form.save()
			return redirect('users/profile')
		except ValueError as e:
			print e
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)

	return HttpResponse(render(request, 'users/form.html', context={'forms': {profile_form}, 'title': 'Update Profile'}))

def register(request):
	if request.method == 'POST':	
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = RegisterForm()
	return HttpResponse(render(request, 'users/form.html', context={'forms': {form}, 'title': 'Register'}))
