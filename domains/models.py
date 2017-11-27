# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
