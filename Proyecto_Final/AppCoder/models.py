from django.db import models

# Create your models here.
#class Curso(models.Model):
#    nombre = models.CharField(max_length=40)
#    camada = models.IntegerField()
    
#class Estudiante(models.Model):
 #   nombre = models.CharField(max_length=40)
  #  apellido = models.CharField(max_length=40)
  #  email = models.EmailField()
    
#class Profesor(models.Model):
 #   nombre = models.CharField(max_length=40)
  #  apellido = models.CharField(max_length=40)
   # email = models.EmailField()
    #profesion = models.CharField(max_length=40)

#class Entregable(models.Model):
 #   nombre = models.CharField(max_length=40)
  #  fechaDeEntrega = models.DateField()
   # entregado = models.BooleanField()

class Autos(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.IntegerField()
    tipo = models.CharField(max_length=40)
    entregado = models.BooleanField()


class Inmuebles(models.Model):

    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    anio = models.IntegerField()

class Facultad(models.Model):

    anio = models.IntegerField()
    carrera = models.CharField(max_length=40)
    universidad = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, default="", editable = False)