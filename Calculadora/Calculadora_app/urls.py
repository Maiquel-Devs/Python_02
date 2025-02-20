from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora_views, name='calculadora')
]


# views.calculadora_views


#.calculadora_viwes é uma função do viwes.py