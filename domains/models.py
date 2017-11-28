# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from django.core.management import call_command
from django.utils import timezone

from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.

class Domain(models.Model):
  default_serial = datetime.today().strftime("%Y%m%d") + "00"
  
#  id = models.AutoField(primary_key=True, default='1')
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(User, related_name='domain_owner', blank=True, default='1')

  serial_number = models.IntegerField(default=default_serial) 

  ttl = models.IntegerField(default='300')

  root_name = models.CharField(max_length=255, default='root.conrey.us')
  refresh = models.IntegerField(default='28880')
  retry   = models.IntegerField(default='3600')
  expire  = models.IntegerField(default='86400')
  minimum = models.IntegerField(default='3600')

  date_created = models.DateTimeField(auto_now=True)
  date_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class RecordType(models.Model):
  name = models.CharField(max_length=5)
  
  date_created = models.DateTimeField
  date_modified = models.DateTimeField

  def __str__(self):
    return self.name

class Record(models.Model):
  name = models.CharField(max_length=255)
  domain = models.ForeignKey(Domain)
  record_type = models.ForeignKey(RecordType, related_name='record_type')
  ttl = models.IntegerField(default=300)
  content = models.CharField(max_length=255)
  date_created = models.DateTimeField
  date_modified = models.DateTimeField
  date_created = models.DateTimeField
  date_modified = models.DateTimeField

  def __str__(self):
    return "{0}.{1}.".format(self.name, self.domain.name)

  def get_record(self):
    return "{0}".format(self.name)

  def get_fqdn(self):
    return "{0}.{1}".format(self.name, self.domain.name)

def zone_update(domain):
  print 'Zone update'
  print 'Domain: {0}'.format(domain.name)
  call_command('update_zone_file', domain.name) 

@receiver(pre_save)
def update_zone_serial(sender, instance, *args, **kwargs):
  if sender.__name__ == "Domain":
    instance.serial_number += 1
  if sender.__name__ == "Record":
    domain = Domain.objects.filter(pk=instance.domain.id).get()
    #values_list('serial_number', flat=True)
    new_serial_number = domain.serial_number + 1
    if Domain.objects.filter(pk=instance.domain.id).update(serial_number = new_serial_number):
    	return True
    else:
    	return False

@receiver(post_save)
def update_zone_file(sender, **kwargs):
  target = kwargs['instance']
  target_name = None

  if sender.__name__ == "Domain":
  	target_name = target
  if sender.__name__ == "Record":
  	target_name = target.domain.name
  
  if target_name is not None:
  	call_command('update_zone_file', target_name)

@receiver(post_delete)
def remove_from_zone_file(sender, **kwargs):
  target = kwargs['instance']

