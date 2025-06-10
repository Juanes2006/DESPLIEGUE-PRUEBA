from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.panel_administrador, name='panel_administrador'),
    path('admin/crear-candidato/', views.crear_candidato, name='crear_candidato'),  # Definirás esta vista después
]
