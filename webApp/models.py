#models.py
from django.db import models
import uuid

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
    
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField (default=uuid.uuid4,editable=False)
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Formulario de Contacto: ({self.id}) - {self.customer_email}"

class SuscripcionForm(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"correos newslatter {self.email}"
    
    