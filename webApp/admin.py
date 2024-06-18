#admin.py
from django.contrib import admin
from .models import flan, ContactForm, SuscripcionForm

# Registra tu modelo aquí
admin.site.register(flan)
admin.site.register(ContactForm)
admin.site.register(SuscripcionForm)

