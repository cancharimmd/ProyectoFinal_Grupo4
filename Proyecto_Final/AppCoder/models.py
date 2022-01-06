from django.db import models

class Vacunas(models.Model):
    INTENSIDAD = (
        (1, 'Poco'),
        (2, 'Normal'),
        (3, 'Mucho'),
        )

    proveedor = models.CharField(max_length=40)
    fecha_creacion = models.DateField()
    pais_origen = models.CharField(max_length=40)
    grado_de_dolor = models.IntegerField(default = 0, choices= INTENSIDAD)

    def __str__(self):
        return f"Vacuna de proveedor {self.proveedor} - Creado el {self.fecha_creacion} - Creado en {self.pais_origen} - Con un grado de dolor : {self.grado_de_dolor}"

class Inmuebles(models.Model):

    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):
        return f"INMUEBLE: Dirección {self.direccion} - Ciudad {self.ciudad} - Año {self.anio}"
class Facultad(models.Model):

    anio = models.IntegerField()
    carrera = models.CharField(max_length=40)
    universidad = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, default="", editable = False)
 
    def __str__(self):
        return f"FACULTAD: Año {self.anio} - Carrera {self.carrera} - Universidad {self.universidad} - Email {self.email}"