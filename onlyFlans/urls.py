"""
urls.py
URL configuration for onlyFlans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from webApp.views import inicio, nosotros, bienvenido,contacto, login_view,logout_view, registro, subscribe, success
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros' ),
    path('bienvenido/', bienvenido, name='bienvenido' ),
    path('contacto/', contacto, name='contacto' ),
    path('login/', login_view, name='login' ), # loguearse
    path('logout/', logout_view, name='logout' ),
    path('registro/', registro, name='registro' ),
    path('subscribe/', subscribe, name='subscribe'), #formulario newslatter
    path('success/', success, name='success'), # /mensaje de recibido o suscrito correctamente
    path('accounts/', include ('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='inicio/', permanent=True)),  # Redirigir la URL raíz a 'inicio/'
    
    
]
