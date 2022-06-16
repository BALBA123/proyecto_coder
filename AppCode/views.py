from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from AppCode.models import cursos


# Create your views here.

#aca vemos 3 textos que se podrian escribir igual pero representarian 3 cosas distintas todos podrian ser 'curso'
#tenemos la clase 'cursos', la funcion 'curso' y la variable dentro de la funcion 'Curso'





def cursoFunc(self):

    Curso = cursos(nombre = "web", camada = "1" )

    Curso.save()

    Curso2 = cursos(nombre="desarrollo back!", camada="2222")

    Curso2.save()

    Document = f"El curso es : {curso.nombre}, la camada: {curso.camada}"


    return HttpResponse(Document)



def inicio(request):
    return render(request, "AppCode/inicio.html") #seguro lo tengo que cambiar por templates

def curso(request):
    return render(request, "Appcode/curso.html") #seguro lo tengo que cambiar por templates

def profesores(request):
    return render(request, "AppCode/profesores.html") #seguro lo tengo que cambiar por templates

def estudiantes(request):
    return render(request, "AppCode/estudiantes.html") #seguro lo tengo que cambiar por templates

def entregables(request):
    return render(request, "AppCode/entregables.html") #seguro lo tengo que cambiar por templates

