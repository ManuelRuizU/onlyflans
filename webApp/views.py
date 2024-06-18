# views.py
from django.shortcuts import render, redirect
from .models import flan

# Create your views here.
def inicio(request):
    flanes_publicos = flan.objects.filter(is_prived=False)  # Obtén todos los flanes de la base de datos
    context = {
        "lista_flanes": flanes_publicos
    }
    return render(request, "inicio.html", context)

def nosotros(request):
    return render(request, "nosotros.html", {})

def bienvenido(request):
    flanes_privados = flan.objects.filter(is_prived=True)
    context = {
        "lista_flanes": flanes_privados
    }
    return render(request, "bienvenido.html", context)

def login(request):
    if request.method == "GET":
        return render(request, "login.html", {})  
    if request.method == "POST":
        
        return redirect("bienvenido")  


