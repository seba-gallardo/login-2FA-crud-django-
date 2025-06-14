from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm, RegistroForm, TwoFactorForm, Setup2FAForm
from .models import Usuario
import qrcode
import io
import base64

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Si el usuario tiene 2FA habilitado, redirigir a verificación 2FA
                if user.is_2fa_enabled:
                    request.session['pre_2fa_user_id'] = user.id
                    return redirect('verify_2fa')
                else:
                    login(request, user)
                    return redirect('inicio')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'auth_app/login.html', {'form': form})

def verify_2fa_view(request):
    if 'pre_2fa_user_id' not in request.session:
        return redirect('login')
    
    user_id = request.session['pre_2fa_user_id']
    try:
        user = Usuario.objects.get(id=user_id)
    except Usuario.DoesNotExist:
        return redirect('login')
    
    if request.method == 'POST':
        form = TwoFactorForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            if user.verify_totp(token):
                # Código correcto, hacer login
                login(request, user)
                del request.session['pre_2fa_user_id']
                return redirect('inicio')
            else:
                form.add_error('token', 'Código de verificación incorrecto.')
    else:
        form = TwoFactorForm()
    
    return render(request, 'auth_app/verify_2fa.html', {'form': form})

@login_required
def setup_2fa_view(request):
    user = request.user
    
    if request.method == 'POST':
        form = Setup2FAForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            if user.verify_totp(token):
                user.is_2fa_enabled = True
                user.save()
                messages.success(request, '2FA configurado exitosamente!')
                return redirect('inicio')
            else:
                form.add_error('token', 'Código de verificación incorrecto.')
    else:
        form = Setup2FAForm()
        # Generar secreto si no existe
        user.generate_totp_secret()
    
    # Generar código QR
    qr_uri = user.get_totp_uri()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_uri)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    context = {
        'form': form,
        'qr_code': qr_code_base64,
        'secret': user.totp_secret,
        'is_2fa_enabled': user.is_2fa_enabled
    }
    
    return render(request, 'auth_app/setup_2fa.html', context)

@login_required
def disable_2fa_view(request):
    if request.method == 'POST':
        user = request.user
        user.is_2fa_enabled = False
        user.totp_secret = None
        user.save()
        messages.success(request, '2FA deshabilitado exitosamente!')
    return redirect('inicio')

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