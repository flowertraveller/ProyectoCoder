from django import forms

class AlumnosFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    
class ProfesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    instrumento = forms.CharField(max_length=40)
    
    