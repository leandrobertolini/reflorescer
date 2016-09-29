# coding: utf-8
from django.db import models
from django.utils import timezone
from .componente import Componente
from .choices import PRESENCA

# Create your models here.
class Ensaio(models.Model):

    data_ensaio =  models.DateField(default=timezone.now, null=True, blank=True)
    componente = models.ForeignKey(Componente, null=True, blank=True)
    presenca = models.CharField(max_length=20, choices=PRESENCA)