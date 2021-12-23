from django.urls import path
from AppCoder import views


urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('profesores', views.profesores, name="Profesores"),
    path('busquedaAlumnos', views.busquedaAlumnos),
    path('profesFormulario', views.profesFomulario),
    path('leerAlumnos', views.leerAlumnos, name="LeerAlumnos"),
    path('eliminarAlumnos/<apellido_para_borrar>/', views.eliminarAlumnos, name="EliminarAlumnos"),
    path('buscar/', views.buscar),
    
]
