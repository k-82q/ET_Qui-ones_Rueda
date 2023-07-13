from django.shortcuts import render, redirect
from .models import Garden, detalle_boleta, Boleta
from .forms import GardenForm, RegistroUserForm
from garden.compra import Carrito
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'index.html')

def  contactenos(request):
    return render(request, 'contactenos.html')

def galeria(request):
    productos= Garden.objects.all()
    datos={
        'productos': productos
    }
    return render(request, 'galeria.html', datos)

def mision(request):
    return render(request, 'mision.html')

def login(request):
    return render(request, 'login.html')

def registrar(request):
    data = {
        'form': RegistroUserForm()
    }
    if request.method == "POST":
        formulario = RegistroUserForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"],
            password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html', data)


def es_superusuario(user):
    return user.is_superuser


@user_passes_test(es_superusuario)
def crear(request):
    if request.method=="POST":
        gardenform = GardenForm(request.POST, request.FILES)
        if gardenform.is_valid():
            gardenform.save()     #similar al insert
            return redirect('index')
    else:
        gardenform=GardenForm()
    return render(request, 'crear.html', {'gardenform':gardenform})

@user_passes_test(es_superusuario)
def eliminar(request, id): 
    gardenEliminado = Garden.objects.get(marca=id) #similar a select * from... where...
    gardenEliminado.delete()
    return redirect ('crear')

@user_passes_test(es_superusuario)
def modificar(request, id): 
    gardenModificado=Garden.objects.get(marca=id) #buscamos el objeto
    datos ={
        'form':GardenForm(instance=gardenModificado)
    }
    if request.method=="POST":
        formulario = GardenForm(data=request.POST, instance=gardenModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect ('productos')
    return render(request, 'modificar.html', datos)

def lol(request):
    return render(request,'lol.html')

def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    garden = Garden.objects.get(marca=id)
    carrito_compra.agregar(garden = garden)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    garden = Garden.objects.get(marca=id)
    carrito_compra.eliminar(garden=garden)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    garden = Garden.objects.get(marca=id)
    carrito_compra.restar(garden=garden)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')   

@login_required
def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad']+int(value['envio']))
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Garden.objects.get(marca = value['marca'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = detalle_boleta(id_boleta = boleta,
                                 id_producto = producto,
                                 cantidad = cant,
                                 subtotal = subtotal)
        detalle.save()
        productos.append(detalle)
    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total,
        
        
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html', datos)

def tienda(request):
    productos = Garden.objects.all()
    page=request.GET.get('page',1)

    try:
        paginator=Paginator(productos,10)
        productos=paginator.page(page)
    except:
        raise Http404

    datos={
        'productos':productos,
        'paginator' : paginator
    }

    return render(request, 'tienda.html', datos)

def productos(request):
    prod = Garden.objects.raw('Select * from garden_Garden')
    datos={
        'garden':prod
    }
    return render(request, 'productos.html', datos)