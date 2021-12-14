from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import AutoFormulario, InmuebleFormulario, FacultadFormulario
from AppCoder.models import Autos, Inmuebles, Facultad



# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def autos(request):
    return render(request, "AppCoder/autos.html")

def inmuebles(request):
    return render(request,"AppCoder/inmuebles.html")

def facultad(request):
    return render(request,"AppCoder/facultad.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")

def autoFormulario(request):
    if request.method == 'POST':
        miFormulario = AutoFormulario(request.POST)        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            abc = Autos(marca=informacion['marca'],modelo=informacion['modelo'],tipo=informacion['tipo'],entregado=informacion['entregado'])
            abc.save()
            return render(request,"AppCoder/inicio.html")
    else:
        
        miFormulario = AutoFormulario()
        
    return render(request,"AppCoder/autoFormulario.html", {"miFormulario": miFormulario})

def inmuebleFormulario(request):
    if request.method == 'POST':
        miFormulario2 = InmuebleFormulario(request.POST)        
        if miFormulario2.is_valid():
            informacion = miFormulario2.cleaned_data
            abc = Inmuebles(direccion=informacion['direccion'],ciudad=informacion['ciudad'],anio=informacion['anio'])
            abc.save()
            return render(request,"AppCoder/inicio.html")
    else:
        
        miFormulario2 = InmuebleFormulario()
        
    return render(request,"AppCoder/inmuebleFormulario.html", {"miFormulario2": miFormulario2})

def facultadFormulario(request):
    if request.method == 'POST':
        miFormulario3 = FacultadFormulario(request.POST)        
        if miFormulario3.is_valid():
            informacion = miFormulario3.cleaned_data
            abc = Facultad(anio=informacion['anio'],carrera=informacion['carrera'],universidad=informacion['universidad'],email=informacion['email'])
            abc.save()
            return render(request,"AppCoder/inicio.html")
    else:
        
        miFormulario3 = FacultadFormulario()
        
    return render(request,"AppCoder/facultadFormulario.html", {"miFormulario3": miFormulario3})