from django.urls import path
from AppCoder import views

urlpatterns = [
    
    path('inicio', views.inicio, name='inicio'),
    path('autos', views.autos, name="autos"),
    path('inmuebles', views.inmuebles, name="inmuebles"),
    path('facultad', views.facultad, name="facultad"),
    path('autoFormulario', views.autoFormulario, name="autoFormulario"),
    path('inmuebleFormulario', views.inmuebleFormulario, name="inmuebleFormulario"),
    path('facultadFormulario', views.facultadFormulario, name="facultadFormulario"),
]