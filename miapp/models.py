from django.db import models

# 📦 Modelo Producto
class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    producto = models.CharField(max_length=100)
    unidad = models.CharField(max_length=45)
    precioCompra = models.DecimalField(max_digits=7, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto

# 🏢 Modelo Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=250)
    rtn = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

# 🛒 Modelo Compra
class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)  
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=50, choices=[('completada', 'Completada'), ('cancelada', 'Cancelada')], default='completada')

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor.nombre} - {self.fecha_compra}"

# 📑 Modelo DetalleCompra
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(max_digits=7, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_compra
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.producto} - Compra {self.compra.id}"

# 📦 Modelo Inventario (Stock por Producto)
class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad_actual = models.IntegerField(default=0)  # Permitir stock negativo si hay errores en Kardex

    def __str__(self):
        return f"{self.producto.producto} - Stock: {self.cantidad_actual}"

    def actualizar_stock(self):
        """ Calcula el stock sumando entradas y restando salidas del Kardex. """
        entradas = Kardex.objects.filter(producto=self.producto, tipo_movimiento='entrada').aggregate(total=models.Sum('cantidad'))['total'] or 0
        salidas = Kardex.objects.filter(producto=self.producto, tipo_movimiento='salida').aggregate(total=models.Sum('cantidad'))['total'] or 0
        self.cantidad_actual = entradas - salidas
        self.save()

# 📊 Modelo Kardex (Movimientos de Inventario)
class Kardex(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_movimiento.capitalize()} {self.cantidad} {self.producto.unidad} - {self.producto.producto}"

    def save(self, *args, **kwargs):
        """ Al guardar un movimiento, actualizar o crear el stock en Inventario. """
        super().save(*args, **kwargs)

        # Obtener o crear inventario del producto
        inventario, created = Inventario.objects.get_or_create(producto=self.producto)

        # Actualizar el stock basado en Kardex
        inventario.actualizar_stock()
