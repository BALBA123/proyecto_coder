from django.urls import path

from AppCode import views

urlpatterns = [
   
    path('inicio', views.inicio), #esta era nuestra primer view
    path('curso', views.curso),
    #path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables, name="entregables"),# esta url tiene "name" para que pueda ser llamada desde un boton en los html(padre)

    path('cursos', views.cursoFunc, name="Cursos"), # este tira error... a buscar. 
            #ya anda habia cambiado los models y no habia echo un migrate por lo que no coincidia el model con la base de datos
    path('cursoFormulario', views.cursoFormularios, name="cursoFormulario"),
    path('profesores', views.profesorFormulario, name="profesores"),


    path('buscador', views.buscador, name="buscador"),
    path('buscar/', views.buscar, name="buscar"),

]


#, name="Cursos" esto estaba despues de views.cursos