# coding: utf-8
from django.db import models
from django.utils import timezone
from .componente import Componente
from .ala import Ala
from .choices import PRESENCA


# Create your models here.
class Ensaio(models.Model):

    data_ensaio = models.DateField(default=timezone.now, null=True, blank=True)
    componente = models.ManyToManyField(Componente)
    ala = models.ForeignKey(Ala, null=True, blank=True)
    presenca = models.CharField(max_length=20, choices=PRESENCA)
