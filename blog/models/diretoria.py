# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from .ala import Ala


# Create your models here.
class Diretoria(models.Model):

    ala = models.ForeignKey(Ala, null=True, blank=True)
    diretor = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return 'Diretoria: {} {}'.format(self.ala, self.diretor)
