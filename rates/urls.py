from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('', views.rates_list, name='rates_list'),  # Ruta para mostrar la lista de tarifas
    path('add/', views.add_rate, name='add_rate'),  # Ruta para agregar una nueva tarifa
    path('update/<int:rate_id>/', views.update_rate, name='update_rate'),  # Ruta para actualizar una tarifa existente
    path('delete/<int:rate_id>/', views.delete_rate, name='delete_rate'),  # Ruta para eliminar una tarifa existente
]
