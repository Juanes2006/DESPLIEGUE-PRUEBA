from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Evaluacion

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('rol', 'documento_identidad', 'nombre', 'institucion')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('rol', 'documento_identidad', 'nombre', 'institucion')}),
    )
    list_display = ['username', 'email', 'rol', 'is_staff']
    search_fields = ['username', 'email', 'rol', 'documento_identidad', 'nombre', 'institucion']
    list_filter = ['rol', 'is_staff', 'is_superuser', 'is_active']
    ordering = ['username']
    readonly_fields = ['last_login', 'date_joined']
admin.site.register(Usuario, UsuarioAdmin)


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['texto', 'opcion_1', 'opcion_2', 'opcion_3', 'respuesta_correcta']
    search_fields = ['texto', 'opcion_1', 'opcion_2', 'opcion_3']
    list_filter = ['respuesta_correcta']
    ordering = ['texto']
admin.site.register(Evaluacion, PreguntaAdmin)


# No necesitas definir el modelo Usuario aquí, ya que debe estar en models.py.
# Pero te ayudo a corregir los campos de UsuarioAdmin según tu modelo personalizado:

