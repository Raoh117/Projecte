from __future__ import unicode_literals

from django.db import models
from articles.models import Article
from django.contrib.auth.models import User

# Create your models here.

class Carret(models.Model):
    usuari = models.ForeignKey(User)
    preu_total = models.DecimalField(max_digits=7,decimal_places=2,  default=0)
    
class Comanda(models.Model):
    carro = models.ForeignKey(Carret)
    article = models.ForeignKey(Article, related_name='article_agafat')
    preu = models.DecimalField(max_digits=7,decimal_places=2)
    quantitat = models.IntegerField()
    data = models.DateField(auto_now=True)


