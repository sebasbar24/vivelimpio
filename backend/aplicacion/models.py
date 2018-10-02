from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=100)
    noticias = models.BooleanField()
    telefono = models.CharField(max_length=20)
    codigo = models.CharField(max_length=200)
    #El foreign key solo permite escoger un item
    zona = models.ForeignKey(Curso, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre

class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    servicio = models.ForeignKey()
    def __str__(self):
        return self.nombre

class Dia(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    dia = models.ManyToManyField(Dia)
    def __str__(self):
        return self.nombre