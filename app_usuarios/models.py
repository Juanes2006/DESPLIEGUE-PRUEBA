from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN_EVENTO = 'ADMIN_EVENTO', 'Administrador de Evento'
        CANDIDATO = 'CANDIDATO', 'Candidato'
        SUPERADMIN = 'SUPERADMIN', 'Super Admin'

    rol = models.CharField(max_length=30, choices=Roles.choices, default=Roles.CANDIDATO)

    # Otros campos opcionales
    documento_identidad = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    institucion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"
    
    
class Evaluacion(models.Model):
    texto = models.CharField(max_length=255)
    opcion_1 = models.CharField(max_length=100)
    opcion_2 = models.CharField(max_length=100)
    opcion_3 = models.CharField(max_length=100)
    OPCIONES = (
        (1, 'Opción 1'),
        (2, 'Opción 2'),
        (3, 'Opción 3'),
    )
    respuesta_correcta = models.PositiveSmallIntegerField(choices=OPCIONES)

    def __str__(self):
        return self.texto
    
    def get_opciones(self):
        return [self.opcion_1, self.opcion_2, self.opcion_3]