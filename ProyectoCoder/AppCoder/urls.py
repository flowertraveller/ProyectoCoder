from django.urls import path
from AppCoder import views




urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    #path('cursos', views.cursos, name="Cursos"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('profesores', views.profesores, name="Profesores"),
    path('profesFormulario', views.profesFormulario),
    path('buscar/', views.buscar),
    
    path('alumnoFormulario', views.alumnoFormulario, name="AlumnoFormulario"),
    path('editarAlumno/<apellido_para_editar>/', views.editarAlumno, name="EditarAlumno"),
    path('leerAlumnos', views.leerAlumnos, name="LeerAlumnos"),
    path('busquedaAlumnos', views.busquedaAlumnos),
    path('eliminarAlumnos/<apellido_para_borrar>/', views.eliminarAlumnos, name="EliminarAlumnos"),
     #PARA CLASES BASADAS EN VISTAS
    path('cursos', views.CursosList.as_view(), name='Cursos'),
   
 ] 
