from django import forms
from .models import Curso, Profesor, Estudiante, Entregable

# Curso
class Cursoformulario(forms.Form):
    nombre = forms.CharField()  
    apellido = forms.CharField()
    camada = forms.IntegerField() 

# profesor    

class Profesorformulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']

# estudiante     

class Estudianteformulario(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']


# entregable  

class Entregableformulario(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fechaDeEntrega', 'entregado']