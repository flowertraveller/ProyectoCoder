from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse, request
from AppCoder.models import Alumnos, Profesores, Cursos, Cursos
from AppCoder.forms import ProfesFormulario, AlumnosFormulario, AlumnoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
#Primer Vista
def inicio(request):
    return render(request,'AppCoder/inicio.html' )

def cursos(request):
    return render(request,'AppCoder/cursos.html' )

def profesores(request):
    return render(request,'AppCoder/profesores.html' )

#FORMULARIOS
#ALUMNOS
def alumnos(request):
    if request.method == "POST":
        miFormulario = AlumnosFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            alumnosInsta = Alumnos(
                            nombre = informacion["nombre"] , 
                            apellido = informacion["apellido"] , 
                            edad = informacion["edad"] )
            alumnosInsta.save()
            return render(request, 'AppCoder/inicio.html')
        
    else:
        miFormulario = AlumnosFormulario()
        
    return render(request,'AppCoder/alumnos.html', {"miFormulario": miFormulario})

#PROFESORES
def profesFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesInsta = Profesores(
                        nombre = informacion["nombre"] ,
                        apellido = informacion["apellido"] , 
                        edad = informacion["edad"],
                        instrumento = informacion["instrumento"] )
            profesInsta.save()
            return render(request, 'AppCoder/inicio.html')
        
    else:
        miFormulario = ProfesFormulario()
        
    return render(request,'AppCoder/profesFormulario.html', {"miFormulario": miFormulario})

#MODIFICAR ALUMNOS
def alumnoFormulario(request):
    if request.method == "POST":
        miFormulario = AlumnoFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            alu = Alumnos(
                        nombre = informacion["nombre"] ,
                        apellido = informacion["apellido"] , 
                        edad = informacion["edad"] )
            
            alu.save()
            return render(request, 'AppCoder/inicio.html')
        
    else:
        miFormulario = AlumnoFormulario()
        
    return render(request,'AppCoder/alumnoFormulario.html', {"miFormulario": miFormulario})
#FIN DE FORMULARIOS

def busquedaAlumnos(request): 
     return render(request, 'AppCoder/busquedaAlumnos.html')
 
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumnos.objects.filter(nombre__icontains=nombre)
        
        return render(request, "AppCoder/busquedaAlumnosRdo.html",{"alumnos":alumnos, "nombre": nombre })
    
    else: 
        respuesta = "Por favor, enviar información"
    return HttpResponse(respuesta)

def leerAlumnos(request):
    alumnos = Alumnos.objects.all()
    dir = {"alumnos":alumnos} #contexto
    return render(request, "AppCoder/leerAlumnos.html", dir)

def eliminarAlumnos(request, apellido_para_borrar):
    alumnoQueQuieroBorrar = Alumnos.objects.get(apellido=apellido_para_borrar)
    alumnoQueQuieroBorrar.delete()
    alumnos = Alumnos.objects.all() 
    return render(request, "AppCoder/leerAlumnos.html", {"alumnos":alumnos})

def editarAlumno (request, apellido_para_editar):
    alumnos = Alumnos.objects.get(apellido=apellido_para_editar)
     
    if request.method == "POST":
        miFormulario = AlumnoFormulario(request.POST)
         
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
          
            alumnos.nombre = informacion["nombre"] 
            alumnos.apellido = informacion["apellido"]
            alumnos.edad = informacion["edad"]
            alumnos.save()           
            
            return render(request, 'AppCoder/inicio.html')
            
    else:
            miFormulario = AlumnoFormulario(initial= 
                            {"nombre":alumnos.nombre, 
                             "apellido": alumnos.apellido, 
                             "edad": alumnos.edad})
            
    return render(request,'AppCoder/editarAlumno.html', 
                {"miFormulario": miFormulario ,
                 "apellido_para_editar":apellido_para_editar})

# CBV (clases pasadas en vistas) ----> CRUD (Create, Read, Update, Delete) con CURSOS
#Leer --- nos da todos los cursos que hay

class CursosList(ListView):
    model = Cursos
    template_name = "AppCoder/cursos.html"

class CursosDetail(DetailView):
    model = Cursos
    template_name = "AppCoder/cursos_detail.html"

class CursosCreate(CreateView):
    model = Cursos
    success_url = "cursos"  
    fields = ["nombre", "camada"]
    
class CursosUpdate(UpdateView):
    model = Cursos
    success_url = "../cursos"
    fields = ["nombre", "camada"]
    
class CursosDelete(DeleteView):
    model = Cursos
    success_url = "../cursos"

#Para el login
def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password = password)
            
            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario} Rockstar"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Error, seguí rockeandola"})

        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Formulario erróneo"})
                
    form = AuthenticationForm() #formulario sin anda para hacer el login
    return render(request, "AppCoder/login.html", {"form": form})

    
    
