from django.shortcuts import render
from django.http import HttpResponse, request
from AppCoder.models import Alumnos, Profesores
from AppCoder.forms import ProfesFormulario, AlumnosFormulario


# Create your views here.
#Primer Vista
def inicio(request):

    return render(request,'AppCoder/inicio.html' )

def cursos(request):

    return render(request,'AppCoder/cursos.html' )

def profesores(request):

    return render(request,'AppCoder/profesores.html' )

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

def profesFomulario(request):
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