# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import flan
from .models import ContactForm
from .forms import ContactFormForm
from .forms import SuscripcionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout



# Create your views here.
def inicio(request):
    flanes_publicos = flan.objects.filter(is_prived=False)  
    context = {
        "lista_flanes": flanes_publicos
    }
    return render(request, "inicio.html", context)

def nosotros(request):
    return render(request, "nosotros.html", {})

@login_required
def bienvenido(request):
    flanes_privados = flan.objects.filter(is_prived=True)
    
  # Obtener el nombre de usuario
    nombre_usuario = request.user.username

    # Personalizar el mensaje de bienvenida
    mensaje_bienvenida = f"¡Hola, {nombre_usuario}! Has iniciado sesión correctamente."

    context = {
        "lista_flanes": flanes_privados,
        "mensaje_bienvenida": mensaje_bienvenida
    }
    return render(request, "bienvenido.html", context)

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('inicio')  # Redirige a la página principal u otra página según sea necesario
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

    
def logout_view(request):
    auth_logout(request)
    return redirect("inicio")



def registro(request):
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        
        user = User.objects.create_user(username, email, password)
        
        # Actualizar campos y luego guardar nuevamente
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.save()
    return redirect("/login")

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

