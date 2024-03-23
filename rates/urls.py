from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views
from .views import rates_list

urlpatterns = [
    path('', rates_list, name='rate')
]
