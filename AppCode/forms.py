from django import forms


class CursoFormulario(forms.Form):

    #especificar los campos
    curso = forms.CharField(max_length= 30)
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    Nombre = forms.CharField(max_length = 30)
    Apellido = forms.CharField(max_length = 30)
    Email = forms.EmailField()
    Profesion = forms.CharField(max_length = 30)