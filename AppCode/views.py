from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from AppCode.models import cursos


# Create your views here.

#aca vemos 3 textos que se podrian escribir igual pero representarian 3 cosas distintas todos podrian ser 'curso'
#tenemos la clase 'cursos', la funcion 'curso' y la variable dentro de la funcion 'Curso'


def curso(self):

    Curso = cursos(nombre = "web", camada = "1" )

    Curso.save()

    Document = f"El curso es : {curso.nombre}, la camada: {curso.camada}"


    return HttpResponse(Document)