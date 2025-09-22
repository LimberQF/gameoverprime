# store/views.py
from django.views.generic import TemplateView
from django.http import Http404
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from datetime import date

from .models import Perfil
from .forms import ProfileForm

# CBVs Catálogo
class HomePage(TemplateView):
    template_name = "home_page.html"

class CategoryListPage(TemplateView):
    template_name = "category.html"

class CategoryDetailPage(TemplateView):
    def get_template_names(self):
        slug = self.kwargs["slug"]
        tpl = f"categories/{slug}.html"
        try:
            get_template(tpl)
        except TemplateDoesNotExist:
            raise Http404("Categoría no encontrada")
        return [tpl]

class CarritoPage(LoginRequiredMixin, TemplateView):
    login_url = 'store:login'
    template_name = "carrito/carrito.html"

class CajaPage(LoginRequiredMixin, TemplateView):
    login_url = 'store:login'
    template_name = "caja/caja.html"

    def dispatch(self, request, *args, **kwargs):
        perfil = getattr(request.user, 'perfil', None)
        rol = (perfil and perfil.rol and perfil.rol.nombre or '').lower()
        if rol not in ('admin', 'cliente'):
            messages.error(request, 'No tienes permisos para acceder a Caja.')
            return redirect('store:home')
        return super().dispatch(request, *args, **kwargs)

# autenticacion
def login_view(request):
    if request.method == 'POST':
        ue = (request.POST.get('usuarioEmail') or '').strip()
        pw = request.POST.get('password') or ''
        remember = request.POST.get('recuerdame') == 'on'

        user = authenticate(request, username=ue, password=pw)
        if user is None:
            try:
                u2 = User.objects.get(email__iexact=ue)
                user = authenticate(request, username=u2.username, password=pw)
            except User.DoesNotExist:
                user = None
        if user is not None:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('store:home')
        messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'register_login/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada.')
    return redirect('store:login')

def register_view(request):
    if request.method == 'POST':
        nombre_completo = (request.POST.get('nombreCompleto') or '').strip()
        username = (request.POST.get('usuario') or '').strip()
        email = (request.POST.get('email') or '').strip()
        password = request.POST.get('password') or ''
        confirm  = request.POST.get('confirmPassword') or ''
        fecha_nac_str = request.POST.get('fechaNacimiento') or ''
        direccion = (request.POST.get('direccion') or '').strip()

        # Validaciones básicas
        if not all([username, email, password, confirm, fecha_nac_str]):
            messages.error(request, 'Completa todos los campos obligatorios.')
            return render(request, 'register_login/registro.html')

        if password != confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'register_login/registro.html')

        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return render(request, 'register_login/registro.html')

        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, 'El correo ya está registrado.')
            return render(request, 'register_login/registro.html')

        # Edad >= 13
        try:
            yyyy, mm, dd = map(int, fecha_nac_str.split('-'))
            fn = date(yyyy, mm, dd)
        except Exception:
            messages.error(request, 'Fecha de nacimiento inválida.')
            return render(request, 'register_login/registro.html')

        hoy = date.today()
        edad = hoy.year - fn.year - ((hoy.month, hoy.day) < (fn.month, fn.day))
        if edad < 13:
            messages.error(request, 'Debes tener al menos 13 años.')
            return render(request, 'register_login/registro.html')

        # Crear usuario
        user = User(username=username, email=email)
        # Partir nombre completo (opcional)
        if nombre_completo:
            partes = nombre_completo.split(' ', 1)
            user.first_name = partes[0]
            if len(partes) > 1:
                user.last_name = partes[1]
        user.set_password(password)
        user.save()

        # Completar perfil
        perfil = user.perfil  # creado por signal
        perfil.direccion = direccion
        perfil.fecha_nacimiento = fn
        perfil.save()

        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return redirect('store:login')

    return render(request, 'register_login/registro.html')

# Perfil
@login_required
def profile_view(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'register_login/profile.html', {'perfil': perfil})

@login_required
def profile_update_view(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'profile_form' in request.POST:
            pform = ProfileForm(request.POST, instance=perfil, user=request.user)
            pwform = PasswordChangeForm(request.user)
            if pform.is_valid():
                pform.save()
                messages.success(request, 'Perfil actualizado.')
                return redirect('store:profile')
        elif 'password_form' in request.POST:
            pform = ProfileForm(instance=perfil, user=request.user)
            pwform = PasswordChangeForm(request.user, request.POST)
            if pwform.is_valid():
                user = pwform.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Contraseña cambiada con éxito.')
                return redirect('store:profile')
    else:
        pform = ProfileForm(instance=perfil, user=request.user)
        pwform = PasswordChangeForm(request.user)

    return render(request, 'register_login/profile_edit.html', {
        'pform': pform,
        'pwform': pwform
    })
