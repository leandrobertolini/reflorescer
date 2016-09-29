# coding: utf-8
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Ala(models.Model):

    fs = FileSystemStorage(location='blog/static/logos/')

    nome = models.CharField(max_length=30)
    total_componentes = models.CharField(max_length=3)
    logo = models.ImageField(storage=fs, blank=True)

    def __str__(self):
        return self.nome

    def logo_ala(self):
        return u'<a href="/static/logos/%s" target="_blank"><img src="/static/logos/%s" width="200" height="150" /></a>' % (self.logo.name, self.logo.name)
    logo_ala.allow_tags = True