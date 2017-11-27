# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from managedns import updateZone
# Create your models here.

class Domain(models.Model):
  name = models.CharField(max_length=255)

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
  record_type = models.ForeignKey(RecordType)
  ttl = models.IntegerField(default=300)
  content = models.CharField(max_length=255)
  date_created = models.DateTimeField
  date_modified = models.DateTimeField
  date_created = models.DateTimeField
  date_modified = models.DateTimeField

  def __str__(self):
    return "{0}.{1}".format(self.name, self.domain.name)
  
@receiver(post_save, sender=Record)
def update_zone_file(sender, **kwargs):
  print 'Zone file update'
  target = kwargs['instance']
  print 'Record: {0}'.format(target.name)
  print 'Domain: {0}'.format(target.domain.name)

