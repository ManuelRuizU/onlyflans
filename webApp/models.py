#models.py
from django.db import models

# Create your models here.
class flan(models.Model):
    flan_uuid = models.UUIDField()
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_publico_general = models.IntegerField()
    precio_publico_logueado = models.IntegerField()
    image_url = models.URLField()
    url = models.CharField(max_length=50)
    slug = models.SlugField()
    is_prived = models.BooleanField()
    stock = models.IntegerField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    delated_at = models.DateTimeField(auto_now=True)
    
    # python manage.py makemigrations (crear la migracion)
    # python manage.py migrate (crear las tablas)


    def __str__(self):
        return f"Tipo Producto: ({self.id} - {self.nombre})"
    
    