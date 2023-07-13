import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Cliente(models.Model):
    usuario =models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(  max_length=255, null=True)
    email=models.CharField(max_length=255, null=True)

    def __str__(self) :
        return self.nombre





class Garden(models.Model):
    marca = models.CharField(primary_key=True, max_length=50, blank=True, verbose_name="Marca")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    stock = models.IntegerField(blank=True, null=True, verbose_name="Stock")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")
    
    
    def __str__(self):
        return self.nombre

class Envio(models.Model):
    tipo = models.CharField(primary_key=True, max_length=50,blank=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.SET_NULL,blank=True,null=True)
    precio=models.IntegerField(blank=True, null=True)
 
 
    def __str__(self):
        return self.tipo
    
class Boleta(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.SET_NULL,blank=True,null=True)
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    envio=models.ForeignKey(Envio, on_delete=models.SET_NULL, blank=True, null=True)
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    

    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey(Boleta, blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Garden, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)
    
