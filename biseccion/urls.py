from django.urls import path
from .views import calcular_raiz  # Eliminamos ver_historial porque ya está en mi_proyecto/urls.py

urlpatterns = [
    path('', calcular_raiz, name='calcular_raiz'),  # Calculadora sigue en /biseccion/
]