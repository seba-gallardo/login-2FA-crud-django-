from django.shortcuts import render, get_object_or_404, redirect
from auth_app.models import Usuario
from auth_app.forms import RegistroForm
from .forms import UsuarioEditForm

# Listar usuarios
def listar_usuarios(request):
    #usuarios = Usuario.objects.all()
    usuarios = Usuario.objects.filter(is_superuser=False)
    return render(request, 'MiCrud/listar_usuarios.html', {'usuarios': usuarios})

# Crear usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.email = form.cleaned_data['email']
            usuario.nombre = form.cleaned_data['nombre']
            usuario.apellido_paterno = form.cleaned_data['apellido_paterno']
            usuario.apellido_materno = form.cleaned_data['apellido_materno']
            usuario.genero = form.cleaned_data['genero']
            usuario.save()
            return redirect('listar_usuarios')
    else:
        form = RegistroForm()
    return render(request, 'MiCrud/registro_usuario.html', {'form': form})

# Editar usuario
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'MiCrud/editar_usuario.html', {'form': form})

# Eliminar usuario
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('listar_usuarios')