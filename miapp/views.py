from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from miapp.models import Producto, Inventario, Kardex

# Función Auxiliar para Validar Precios
def validar_precios(precio_compra, precio_venta):
    try:
        precio_compra = float(precio_compra)
        precio_venta = float(precio_venta)
        if precio_compra <= 0 or precio_venta <= 0:
            return "Los precios deben ser valores positivos."
    except ValueError:
        return "Los precios deben ser números."
    return None

# Página de Inicio
def index(request):
    return render(request, 'index.html')

# Secciones de la App
def compras(request):
    return render(request, 'compras.html')

def inventario(request):
    return render(request, 'inventario.html')

def ventas(request):
    return render(request, 'ventas.html')

def servicios(request):
    return render(request, 'servicios.html')

def entradaProductos(request):
    return render(request, 'entradaProductos.html')

def historialCompras(request):
    return render(request, 'historialCompras.html')

def nuevaVenta(request):
    return render(request, 'nuevaVenta.html')

def facturasVenta(request):
    return render(request, 'facturasVenta.html')

#  Vista para Mostrar Productos
def productos(request):
    return render(request, 'productos.html')

