from django.urls import path

from AppCode import views

urlpatterns = [
   
    path('', views.inicio), #esta era nuestra primer view
    path('curso', views.curso),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),

    path('cursos', views.cursoFunc, name="Cursos"), # este tira error... a buscar
]


#, name="Cursos" esto estaba despues de views.cursos