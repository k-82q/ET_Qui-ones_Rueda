from django.urls import path
from garden.views import *

urlpatterns = [
    path('', index, name="index"),
    path('contactenos/', contactenos, name="contactenos"),
    path('galeria/',galeria, name="galeria"),
    path('login/',login, name="login"),
    path('mision/',mision, name="mision"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('crear/', crear, name="crear"),
    path('lol/',lol, name="lol"),
    path('productos/',productos, name="productos"),

    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta, name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]