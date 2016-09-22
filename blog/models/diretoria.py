from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .ala import Ala
from .componente import Componente

# Create your models here.
class Diretoria(models.Model):


    ala = models.ForeignKey(Ala, null=True, blank=True)
    diretor = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return 'Diretoria: {} {}'.format(self.ala, self.diretor)