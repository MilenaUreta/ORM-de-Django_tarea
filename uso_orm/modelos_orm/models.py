from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):
        return self.descripcion


class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
    
    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

    class Meta:
        verbose_name='factura'
        verbose_name_plural='facturas'

    def __str__(self):
     return str(self.total)


class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

    class Meta:
        verbose_name='detalle'
        verbose_name_plural='detalles'
    
    def __str__(self):
     return str(self.cantidad)