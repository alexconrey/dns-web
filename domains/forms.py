from django.forms import ModelForm
from django import forms

from .models import Domain, Nameserver, Record, RecordType

class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ['name', 'nameserver1', 'nameserver2', 'owner', 'ttl', 'root_name', 'refresh', 'retry', 'expire', 'minimum']

class NameserverForm(ModelForm):
    class Meta:
        model = Nameserver
        fields = ['name', 'server']
       
class RecordTypeForm(ModelForm):
    class Meta:
        model = RecordType
        fields = ['name']

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'domain', 'record_type', 'ttl', 'content']
