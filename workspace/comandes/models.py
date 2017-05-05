from __future__ import unicode_literals

from django.db import models
from articles.models import Article
from django.contrib.auth.models import User

# Create your models here.
class Comanda(models.Model):
    id_linia = models.AutoField(primary_key=True)
    id_comanda = models.ForeignKey('Carret')
    id_producte = models.ForeignKey('articles.Article')
    preu = models.DecimalField(max_digits=7, decimal_places=2)
    quantitat = models.IntegerField()
    models.DateField( auto_now_add=True)

class Carret(models.Model):
    id_comanda = models.AutoField(primary_key=True)
    data = models.DateField(auto_now=True)
    usuari = models.ForeignKey(User)

