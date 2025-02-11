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