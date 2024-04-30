from django.urls import path
from .views import home, products, exit, register, user_login
from . import views

urlpatterns = [
    path('products/', products, name="products"),
    path('logout/', exit, name="exit"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),

]

