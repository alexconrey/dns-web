from django.forms import ModelForm
from django import forms

from .models import Domain

class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ['name', 'nameserver1', 'nameserver2']

