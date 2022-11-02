# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class Dispositivo(models.Model):
    Id = models.AutoField(primary_key=True)
    Imei =  models.CharField(max_length=50)
    Sim = models.CharField(max_length=50)
    def __unicode__(self):
        return str(self.Imei)
        
class Historico_Dispositivo(models.Model):
    Id = models.AutoField(primary_key=True)
    Imei =  models.CharField(max_length=50)
    Latitud = models.CharField(max_length=50,blank=True, null=True)
    Longitud = models.CharField(max_length=50,blank=True, null=True)
    Llenado = models.CharField(max_length=50,blank=True, null=True)
    Bateria = models.CharField(max_length=50,blank=True, null=True)
    Humo = models.CharField(max_length=50,blank=True, null=True)
    Volcamiento = models.CharField(max_length=50,blank=True, null=True)
    FechaDispositivo = models.CharField(max_length=50,blank=True, null=True)
    Fecha = models.DateTimeField(default=datetime.now, blank=True)
    def __unicode__(self):
        return str(self.Imei)