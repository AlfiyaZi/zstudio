#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User



class Contact(models.Model):
    name = models.CharField(max_length=128, help_text=u"Имя")
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

