from django.db import models

# Create your models here.

class ResponsableVenta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class VentasRealizadas(models.Model):
    nombre_producto = models.CharField(null=False,max_length=100)
    marca = models.CharField(null=False,max_length=100)
    precio_unidad =  models.IntegerField(blank=False)  # Campo obligatorio
 # Campo obligatorio
    cantidad_vendida = models.IntegerField(blank=False)
    total_venta = models.IntegerField(blank=False)
    responsable_venta = models.ForeignKey(ResponsableVenta, on_delete=models.CASCADE)
    comentario = models.TextField(blank=True)               # aqui el responsable pedira alguna validacion para poder ingresar yo controlo todo
    fecha = models.DateTimeField(auto_now_add=True)

