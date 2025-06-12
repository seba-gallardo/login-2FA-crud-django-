from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                # Agregar error cuando las credenciales son incorrectas
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'auth_app/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'auth_app/registro.html', {'form': form})

@login_required
def inicio_view(request):
    return render(request, 'auth_app/inicio.html', {'usuario': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')