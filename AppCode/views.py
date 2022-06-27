from distutils.log import info
from xml.dom.minidom import Document
from django.shortcuts import render 
from django.http import HttpResponse
from AppCode.models import cursos
from AppCode.forms import cursoFormulario


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



def cursoFormularios(request):
    if request.method == "POST":

        miFormulario = cursoFormulario(request.POST) # aca llega toda la info del HTML

        print(miFormulario)

        if miFormulario.is_valid: #validacion de django
            
            informacion = miFormulario.cleaned_data #

            curso = cursos (nombre=informacion['curso'], camada=informacion['camada'])
            #en el model curso uno de los atributos es 'nombre' que lo completamos con el valor de la key 'curso' del diccionario que nos trae el formulario que es tipo JASON
            curso.save()

            return render(request, "AppCode/curso.html")
    else:

        miFormulario = cursoFormulario() #formulario vacio para construir el HTML
        return render(request, "AppCode/cursoFormulario.html", {"miFormulario":miFormulario})

