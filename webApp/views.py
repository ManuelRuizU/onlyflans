# views.py
from django.shortcuts import render, redirect
from .models import flan
from .models import ContactForm
from .forms import ContactFormForm
from .forms import SuscripcionForm

# Create your views here.
def inicio(request):
    flanes_publicos = flan.objects.filter(is_prived=False)  
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
        email = request.POST.get('email')  
        password = request.POST.get('password')  
    
        request.session["email"] = email  
        
        return redirect("bienvenido")

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Crear una instancia del modelo y guardar los datos del formulario
            contact_form = ContactForm(
                customer_name=form.cleaned_data['customer_name'],
                customer_email=form.cleaned_data['customer_email'],
                message=form.cleaned_data['message']
            )
            contact_form.save()
            return redirect('/')
    else:
        form = ContactFormForm()
    context ={
        "form": form
    }
    return render(request, "contacto.html", context)

def subscribe(request):
    if request.method == 'POST':
        form = SuscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Asegúrate de tener una vista 'success'
    else:
        form = SuscripcionForm()
    return render(request, 'subscribe.html', {'form': form})

def success(request):
    return render(request, 'success.html')

