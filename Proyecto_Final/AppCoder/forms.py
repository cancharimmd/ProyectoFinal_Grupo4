from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    #Obligatorio
    email = forms.EmailField()    
    password1 = forms.CharField(label='Contraseña')    
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
    
class VacunaFormulario(forms.Form):
    
    proveedor = forms.CharField()
    fecha_creacion = forms.DateField()
    pais_origen = forms.CharField()
    grado_de_dolor = forms.IntegerField(required=False, max_value= 3, min_value=1)
    
class InmuebleFormulario(forms.Form):
    
    direccion = forms.CharField()
    ciudad = forms.CharField()
    anio = forms.IntegerField()
    
    
class FacultadFormulario(forms.Form):
    
    anio = forms.IntegerField()
    carrera = forms.CharField()
    universidad = forms.CharField()
    email = forms.EmailField()
    
    
    