from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    SHIRT_SIZES = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande'),
    )

    SHOES = (
    	('33','33'),
		('34','34'),
		('35','35'),
		('36','36'),
		('37','37'),
		('38','38'),
		('39','39'),
		('40','40'),
		('41','41'),
		('42','42'),
		('43','43'),
		('44','44'),
		('45','45'),
    )

    PGTO = (
    	('Em Aberto','Em Aberto'),
    	('Total','Total'),
    	('Carteirinha','Carteirinha'),
    	('Fantasia','Fantasia'),
    )



    responsavel = models.ForeignKey('auth.User')
    nome 		= models.CharField(max_length=400)
    email		= models.CharField(max_length=300)
    cidade 		= models.CharField(max_length=200)
    manequim 	= models.CharField(max_length=2, choices=SHIRT_SIZES)
    calcado 	= models.CharField(max_length=2, choices=SHOES)
    pagamento 	= models.CharField(max_length=20,choices=PGTO)
    obs 		= models.TextField(blank=True,null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome