from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_url, name='create_url'),
    path('view/<str:unique_url>/', views.unique_url_detail, name='unique_url_detail'),
]
