#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SuscripcionForm

class ContactFormForm(forms.Form):
    customer_name = forms.CharField(max_length=50, label='Nombre')
    customer_email = forms.EmailField(label='Correo')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = SuscripcionForm
        fields = ['email']
