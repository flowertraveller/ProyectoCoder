from django.db import models

# Create your models here.
class Cursos (models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"CURSO: {self.nombre} CAMADA: {self.camada}" 

class Alumnos (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"NOMBRE {self.nombre} APELLIDO: {self.apellido} EDAD: {self.edad}" 

class Profesores  (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    instrumento = models.CharField(max_length=40)
    
    def __str__(self):
        return f"NOMBRE {self.nombre} APELLIDO: {self.apellido} EDAD: {self.edad} INSTRUMENTO: {self.instrumento}"