from django.contrib.auth.models import User
from django.db import models
from .models import Garden
class Carrito:
   
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, garden):
        if garden.marca not in self.carrito.keys():
            self.carrito[garden.marca] = {
                "marca": garden.marca,
                "nombre": garden.nombre,
                "precio": str(garden.precio),
                "cantidad": 1,
                "total": garden.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key == garden.marca:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = garden.precio
                    value["total"] = value["total"] + garden.precio
                    break
        garden.stock -= 1
        garden.save()
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, garden):
        id = garden.marca
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, garden):
        for key, value in self.carrito.items():
            if key == garden.marca:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])-garden.precio
                garden.stock += 1
                garden.save()

                if value["cantidad"] < 1:
                    self.eliminar(garden)
                break
        self.guardar_carrito()

    def limpiar(self):
        for key, value in self.carrito.items():
            cantidad = value["cantidad"]
            garden = Garden.objects.get(marca=key)
            garden.stock += cantidad
            garden.save()

        self.session["carrito"] = ()
        self.session.modified = True