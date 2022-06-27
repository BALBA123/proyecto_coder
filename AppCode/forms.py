from django import forms


class cursoFormulario(forms.Form):

    #especificar los campos
    curso = forms.CharField(max_length= 30)
    camada = forms.IntegerField()