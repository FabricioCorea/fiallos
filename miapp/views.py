from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from miapp.models import *

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
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})
# Agregar producto
def agregarProducto(request):
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        producto = request.POST.get('producto')
        unidad = request.POST.get('unidad')
        precioCompra = request.POST.get('precioCompra')
        precioVenta = request.POST.get('precioVenta')
        #imagen = request.FILES.get('imagen')  # Para manejar imágenes
        estado = request.POST.get('estado')

        if codigo and producto and unidad and precioCompra and precioVenta and estado:
            nuevoProducto = Producto(
                codigo=codigo,
                producto=producto,
                unidad=unidad,
                precioCompra=precioCompra,
                precioVenta=precioVenta,
                #imagen=imagen,  
                estado=estado
            )
            nuevoProducto.save()
            messages.success(request, "Producto agregado con éxito.")
        else:
            messages.warning(request, "Hay campos obligatorios vacíos.")
    return redirect('productos') 
# Editar producto
def editarProducto(request, id):
    EditarProducto = Producto.objects.get(id=id)
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        producto = request.POST.get('producto')
        unidad = request.POST.get('unidad')
        precioCompra = request.POST.get('precioCompra')
        precioVenta = request.POST.get('precioVenta')
        #imagen = request.FILES.get('imagen')  # Para manejar imágenes
        estado = request.POST.get('estado')

        if codigo and producto and unidad and precioCompra and precioVenta and estado:
            codigo=EditarProducto.codigo,
            producto=EditarProducto.producto,
            unidad=EditarProducto.unidad,
            precioCompra=EditarProducto.precioCompra,
            precioVenta=EditarProducto.precioVenta,
            #imagen=imagen,  
            estado=EditarProducto.estado
            EditarProducto.save()
            messages.success(request, "Producto actualizado con éxito.")
        else:
            messages.warning(request, "Hay campos obligatorios vacíos.")
    return redirect('productos') 

