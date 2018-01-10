from django.forms import ModelForm
from django import forms

from .models import Server, Region 

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['hostname', 'ip_address', 'location', 'is_active']

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name','location']
