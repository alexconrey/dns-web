# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
      return self.name

class Server(models.Model):
    ACTIVE_CHOICES = (
     ('Y', 'Yes'),
     ('N', 'No'),
    )

    hostname = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=32)
    location = models.ForeignKey(Region)
    active = models.CharField(max_length=2, choices=ACTIVE_CHOICES, default='N')
    ctime = models.DateTimeField()

    def __str__(self):
      return self.hostname


