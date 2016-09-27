from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from .choices import SHIRT_SIZES, SHOES, PGTO, CARTEIRINHA, STATUS
from .ala import Ala

class Componente(models.Model):

    fs = FileSystemStorage(location='blog/static/fotos/')

    responsavel = models.ForeignKey('auth.User')
    nome = models.CharField(max_length=400)
    apelido = models.CharField(max_length=200, blank=True, null=True)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    cidade = models.CharField(max_length=200)
    manequim = models.CharField(max_length=2, choices=SHIRT_SIZES)
    calcado = models.CharField(max_length=2, choices=SHOES)
    ala = models.ForeignKey(Ala, null=True, blank=True)

    pagamento = models.CharField(max_length=20, choices=PGTO)
    carteirinha = models.CharField(max_length=20, choices=CARTEIRINHA)
    obs = models.TextField(blank=True, null=True)
    foto = models.ImageField(storage=fs, blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=15, blank=True, null=True, choices=STATUS)

    def __str__(self):
        return self.nome

    def foto_comp(self):
        return u'<a href="/static/fotos/%s" target="_blank"><img src="/static/fotos/%s" width="150" height="100" /></a>' % (self.foto.name, self.foto.name)
    foto_comp.allow_tags = True