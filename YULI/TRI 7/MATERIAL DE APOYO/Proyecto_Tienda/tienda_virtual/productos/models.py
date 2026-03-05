from django.db import models
from django.conf import settings

# Create your models here.

'''Este modelo representa los productos que se venden dentro de la tienda virtual. Donde tenemos:
- Información básica del producto
- Manejo del stock
- Estado (activo / inactivo)
- Regla automática que desactiva el producto si no hay stock'''


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    #decimal con 10 digitos y 2 decimales
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #almacenar la imagen. Se almacena en la carpeta media
    imagen = models.ImageField(upload_to='productos/')
    #restricción de que solo sean numeros positivos
    stock = models.PositiveIntegerField(default=0)
    #estado del producto
    activo = models.BooleanField(default=True)


    #Este método evita que se pueda vender algun producto que no tenga inventario
    '''El método save ya está creado por defecto en Django, aquí lo estamos sobreescribiendo de acuerdo con
    la regla activo o inactivo que depende del stock'''

    def save(self, *args, **kwargs):
        # Si el stock llega a 0 se desactiva automáticamente
        if self.stock == 0:
            self.activo = False
        #else:
            #self.activo = True

        #Despues de ejecutar la regla, se ejecuta el método save como Django lo realiza
        #si esta línea no se coloca, no se actualiza en bd
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.nombre

