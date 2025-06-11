from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('/auth/login')

urlpatterns = [
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
    
    # Prefijos específicos por app
    path('auth/', include('auth_app.urls')),  # Enlaza las rutas de la app 'auth_app.urls'
    
]

# path('usuarios/', include('crudSeba.urls')), # Enlaza las rutas de la app 'crudSeba.urls'