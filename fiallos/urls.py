"""
URL configuration for fiallos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Módulo de Productos
    path('productos/', views.productos, name='productos'),
    path('nuevoProducto/', views.agregarProducto, name='agregarProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),

    # Módulo de Compras
    path('compras/', views.compras, name='compras'),
    path('historialCompras/', views.historialCompras, name='historialCompras'),

    # Módulo de Inventario
    path('inventario/', views.inventario, name='inventario'),
    path('entradas/', views.entradaProductos, name='entradaProductos'),

    # Módulo de Ventas
    path('ventas/', views.ventas, name='ventas'),
    path('nuevaVenta/', views.nuevaVenta, name='nuevaVenta'),
    path('facturasVenta/', views.facturasVenta, name='facturasVenta'),

    # Módulo de Servicios
    path('servicios/', views.servicios, name='servicios'),
]


