from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    consola = models.CharField(max_length=200)
    preu = models.DecimalField(max_digits=7,decimal_places=2)
    PEGI = models.CharField(max_length=200)
    stock = models.IntegerField()
    companyia = models.CharField(max_length=200)
    usuari_comprador=models.ForeignKey('usuaris.Usuari',on_delete=models.SET_NULL,blank=True, null=True,related_name="articles_comprats")
    imatge = models.ImageField(max_length=200, upload_to='articles')
    coleccionista = models.BooleanField(default=False)
    detalls = models.TextField(null=True, blank=True)
    
    
    
   