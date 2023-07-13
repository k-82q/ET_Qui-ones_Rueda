from socket import fromshare
#from tkinter import Widgets
from django.forms import ModelForm
from django.forms.models import ModelChoiceField
from django import forms
from .models import Garden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['nombre', 'marca', 'precio', 'imagen','stock']
        labels = {
            'nombre': 'Nombre',
            'marca': 'Marca',
            'precio':'Precio',
            'stock': 'Stock',
            'imagen': 'Imagen'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre..',
                    'id':'nombre',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese marca..',
                    'id':'marca',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese precio..',
                    'id':'precio',
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Stock..',
                    'id':'stock',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }#cierre de widgets
