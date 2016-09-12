from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Alas(models.Model):
    nome = models.CharField(max_length=30)
    total_componentes = models.CharField(max_length=3)
    def __str__(self):
        return self.nome

class Componentes(models.Model):

    fs = FileSystemStorage(location='blog/static/fotos/')

    SHIRT_SIZES = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande'),
    )

    SHOES = (
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    )

    PGTO = (
        ('Em Aberto', 'Em Aberto'),
        ('Total', 'Total'),
        ('Carteirinha', 'Carteirinha'),
        ('Fantasia', 'Fantasia'),
    )

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
    ala = models.ForeignKey(Alas, null=True, blank=True)

    pagamento = models.CharField(max_length=20, choices=PGTO)
    obs = models.TextField(blank=True, null=True)
    image = models.ImageField(storage=fs, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

    def foto(self):
        return u'<a href="/static/fotos/%s" target="_blank"><img src="/static/fotos/%s" width="150" height="100" /></a>' % (self.image.name, self.image.name)
    foto.allow_tags = True


