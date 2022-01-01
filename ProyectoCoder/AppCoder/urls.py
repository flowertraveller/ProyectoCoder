from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView  #Para Logout


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
    path(r'^(?P<pk>\d+)$', views.CursosDetail.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursosCreate.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursosUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursosDelete.as_view(), name='Delete'),
    
    #LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    
    #LOGOUT
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    
    #EDITARPERFIL
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    

    
] 
