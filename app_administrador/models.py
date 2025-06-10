
from django.db import models

class Candidato(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    puntaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre
