from django import forms

class AutoFormulario(forms.Form):
    
    marca = forms.CharField()
    modelo = forms.IntegerField()
    tipo = forms.CharField()
    entregado = forms.BooleanField(required=False)
    
class InmuebleFormulario(forms.Form):
    
    direccion = forms.CharField()
    ciudad = forms.CharField()
    anio = forms.IntegerField()
    
    
class FacultadFormulario(forms.Form):
    
    anio = forms.IntegerField()
    carrera = forms.CharField()
    universidad = forms.CharField()
    email = forms.EmailField()
    
    
    