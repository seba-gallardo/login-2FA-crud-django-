from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('verify-2fa/', views.verify_2fa_view, name='verify_2fa'),
    path('setup-2fa/', views.setup_2fa_view, name='setup_2fa'),
    path('disable-2fa/', views.disable_2fa_view, name='disable_2fa'),
    path('registro/', views.registro_view, name='registro'),
    path('inicio/', views.inicio_view, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
]