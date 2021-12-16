from django.db import models

# Create your models here.
class Laptops(models.Model):

    marca = models.CharField(max_length=10)
    pulgadas = models.IntegerField()
    procesador = models.CharField(max_length=20)
    ram = models.CharField(max_length=5)
    precio = models.FloatField()

class Celulares(models.Model):

    marca = models.CharField(max_length=10)
    compania = models.CharField(max_length=10)
    conectividad = models. CharField(max_length=3)
    memoria = models.CharField (max_length=6)
    precio = models.FloatField ()

class Televisores(models.Model):
    
    marca = models.CharField(max_length=10)
    pulgadas = models.IntegerField()
    resolusion = models.CharField(max_length=10)
    precio = models.FloatField()
