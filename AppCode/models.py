from django.db import models
#corremos comando en terminal python manage.py migrate para que nos levante la base de datos db.sqlite3

# Create your models here.

class cursos(models.Model):
    nombre = models.CharField(max_length = 40) # tipo de dato caracteres has 40 caracteres (string)
    camada = models.IntegerField()

class estudiante(models.Model):
    nombre = models.CharField(max_length = 30) # en los campos CharField hay que detallar el max_length si no tira error
    apellido = models.CharField(max_length = 30)
    email = models.EmailField() # tipo de dato email

class profesor(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()
    profesion = models.CharField(max_length = 30)

class entregables(models.Model):
    nombre = models.CharField(max_length = 30)
    fechaDeEntrega = models.DateField() #tipo de dato fecha
    entregado = models.BooleanField() # tipo de dato booleano
