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
#Lo relacionado con mi app ---------------------------------------------------------
from miapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compras/', views.compras, name='compras'),
    path('inventario/', views.inventario, name='inventario'),
    path('ventas/', views.ventas, name='ventas'),
    path('servicios/', views.servicios, name='servicios'),
    path('entradas/', views.entradaProductos, name='entradaProductos'),
    path('productos/', views.productos, name='productos'),
    path('historialCompras/', views.historialCompras, name='historialCompras'),
    path('nuevaVenta/', views.nuevaVenta, name='nuevaVenta'),
    path('facturasVenta/', views.facturasVenta, name='facturasVenta'),
]
