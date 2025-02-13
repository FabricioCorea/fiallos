from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
def productos(request):
    return render(request, 'productos.html')
def historialCompras(request):
    return render(request, 'historialCompras.html')
def nuevaVenta(request):
    return render(request, 'nuevaVenta.html')
def facturasVenta(request):
    return render(request, 'facturasVenta.html')