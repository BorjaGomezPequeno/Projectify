from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('sobre-nosotros/', views.sobre_nosotros, name="sobre-nosotros"),
    path('contacto/', views.contacto, name="contacto"),
]
