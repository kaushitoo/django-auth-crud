from django.db import models

class Cargo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    responsabilidades = models.TextField()
    salario = models.CharField(max_length=14)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)


