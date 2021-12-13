from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Primer Vista
def inicio(request):

    return render(request,'AppCoder/inicio.html' )