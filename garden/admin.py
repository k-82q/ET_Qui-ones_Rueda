from django.contrib import admin
from .models import Garden, detalle_boleta, Boleta,Cliente,Envio

# Register your models here.

admin.site.register(Garden)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)
admin.site.register(Cliente)
admin.site.register(Envio)
