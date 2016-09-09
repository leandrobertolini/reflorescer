from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Post(models.Model):

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

    ALAS = (
        ('Reflorescer', 'Reflorescer'),
        ('Roseira_Real', 'Roseira Real'),
        ('Quebrada', 'Quebrada'),
        ('Compositores', 'Compositores'),
        ('Loucos_pela_Rosas', 'Loucos pela Rosas'),
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
    ala = models.CharField(max_length=40, choices=ALAS)

    pagamento = models.CharField(max_length=20, choices=PGTO)
    obs = models.TextField(blank=True, null=True)
    foto = models.ImageField(storage=fs)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

    def image_tag(self):
        return u'<img src="/static/fotos/%s" width="200" />' % self.foto.name

    image_tag.allow_tags = True
