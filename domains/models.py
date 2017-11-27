# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.management import call_command

from datetime import datetime

# Create your models here.

class Domain(models.Model):
  default_serial = datetime.today().strftime("%Y%m%d") + "00"
 
  name = models.CharField(max_length=255)
  serial_number = models.IntegerField(default=default_serial) 

  date_created = models.DateTimeField
  date_modified = models.DateTimeField

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
  print 'Domain: {0}'.format(domain)
  call_command('update_zone_file', domain) 

@receiver(post_save, sender=Record)
def update_zone_file(sender, **kwargs):
  target = kwargs['instance']
  zone_update(target.domain.name)

@receiver(post_delete, sender=Record)
def remove_from_zone_file(sender, **kwargs):
  target = kwargs['instance']
  zone_update(target.domain.name)

