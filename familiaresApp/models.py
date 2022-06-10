from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    nacimiento = models.DateTimeField()
    edad = models.IntegerField()
    email = models.EmailField()
    
    