from __future__ import unicode_literals

from django.db import models
from usuaris.models import Usuari

# Create your models here.

class Article(models.Model):
    nom = models.CharField(max_length=200)
    consola = models.CharField(max_length=200)
    esconsola = models.BooleanField(default=False)
    preu = models.DecimalField(max_digits=7,decimal_places=2)
    PEGI = models.CharField(max_length=200)
    stock = models.IntegerField()
    companyia = models.CharField(max_length=200)
    imatge = models.ImageField(max_length=200, upload_to='articles')
    coleccionista = models.BooleanField(default=False)
    detalls = models.TextField(null=True, blank=True)
    video = models.CharField(max_length=1000, default="")

    
    
    
   