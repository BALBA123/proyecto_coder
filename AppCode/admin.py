from django.contrib import admin
from .models import * #importamos el archivo models

# Register your models here.

#superusuario:
    #usuario = agustin
    #contraseña = 123

admin.site.register(cursos)

admin.site.register(estudiante)

admin.site.register(profesor)

admin.site.register(entregables)