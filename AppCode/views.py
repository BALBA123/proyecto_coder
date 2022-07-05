from distutils.log import info
import re
from xml.dom.minidom import Document
from django.shortcuts import render 
from django.http import HttpResponse
from AppCode.models import cursos, profesor
from AppCode.forms import CursoFormulario, ProfesorFormulario


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

        miFormulario = CursoFormulario(request.POST) # aca llega toda la info del HTML

        print(miFormulario)

        if miFormulario.is_valid: #validacion de django
            
            informacion = miFormulario.cleaned_data #

            curso = cursos (nombre=informacion['curso'], camada=informacion['camada'])
            #en el model curso uno de los atributos es 'nombre' que lo completamos con el valor de la key 'curso' del diccionario que nos trae el formulario que es tipo JASON
            curso.save()

            return render(request, "AppCode/curso.html")
    else:

        miFormulario = CursoFormulario() #formulario vacio para construir el HTML
        return render(request, "AppCode/cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):
    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            #print(info) #esto muestra el diccionario para ver mejor los datos ya pasados a limpio
            profe = profesor (nombre=info['Nombre'], apellido=info['Apellido'], email=info['Email'], profesion=info['Profesion'])
            # las key´s al pasarce al html se pone la primera letra en mayuscula???
            profe.save()

            return render(request, "AppCode/inicio.html")

    else:
            
        miFormulario = ProfesorFormulario()
        return render(request, "AppCode/profesores.html", {"miFormulario":miFormulario})



def buscador(request):

    return render(request, "AppCode/buscador.html")

def buscar(request):
    #respuesta = f"estoy buscando la camada nro: {request.GET['camada']}"
    #return HttpResponse(respuesta)
    if request.GET['camada']:

        camada =request.GET['camada'] # aca solo renvio lo que piden
        print(camada)
        nombreCurso = cursos.objects.filter(camada__icontains=camada) # este es el verdadero buscador
        print(nombreCurso)
# el buscador entre al modelo cursos, a sus objetos y filtra en la key camada. primer camada es la variable de la funcion y la segunda es la key del diccionario de la base de datos
        return render(request, "AppCode/buscador.html", {"curso":nombreCurso, "camada":camada})

    else:
        respuesta = "no ingresaste numero de camada"

    return render(request, "AppCode/buscador.html")
