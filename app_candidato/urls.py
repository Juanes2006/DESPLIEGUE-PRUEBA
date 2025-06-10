from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.panel_candidato, name='panel_candidato'),
    path('realizar_evaluacion/', views.realizar_evaluacion, name='realizar_evaluacion'),
]
