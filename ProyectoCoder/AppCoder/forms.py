from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AlumnosFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    
class ProfesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    instrumento = forms.CharField(max_length=40)

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    
class CursosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40) 
    camada = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
   
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    imagen_avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2'] 
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    
    class Meta: #Define el modelo, que campos se completan
        model = User
        fields = ['email', 'password1', 'password2'] 
        help_text = {k:"" for k in fields}
   
    
    