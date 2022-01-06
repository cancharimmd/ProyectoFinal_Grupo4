from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('inicio', views.inicio, name='inicio'),
    path('vacunas', views.vacunas, name="vacunas"),
    path('inmuebles', views.inmuebles, name="inmuebles"),
    path('facultad', views.facultad, name="facultad"),
    path('vacunaFormulario', views.vacunaFormulario, name="vacunaFormulario"),
    path('inmuebleFormulario', views.inmuebleFormulario, name="inmuebleFormulario"),
    path('facultadFormulario', views.facultadFormulario, name="facultadFormulario"),
    
    path('eliminarVacuna/<vacuna_proveedor>/', views.eliminarVacunas, name='eliminarVacuna'),
    
    path('vacuna/list', views.VacunaList.as_view(), name = "List"),
    path(r'^(?P<pk>\d+)$', views.VacunaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.VacunaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.VacunaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.VacunaDelete.as_view(), name='Delete'),

    path('login', views.login_request, name = 'Login'), 
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    
]   