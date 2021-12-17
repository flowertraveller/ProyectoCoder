from django import forms

class AlumnosFormulario(forms.Form):
    
    nombre = forms.CharField() 
    apellido = forms.CharField()
    edad = forms.IntegerField()
    
    
    