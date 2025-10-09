from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from .views import (
    HomePage, CategoryListPage, CategoryDetailPage, CarritoPage, CajaPage,
    login_view, logout_view, register_view,
    profile_view, profile_update_view,
)

app_name = "store"

urlpatterns = [
    # Rutas oficiales
    path("", HomePage.as_view(), name="home"),
    path("categorias/", CategoryListPage.as_view(), name="category"),
    path("categorias/<slug:slug>/", CategoryDetailPage.as_view(), name="category_detail"),
    path("carrito/", CarritoPage.as_view(), name="carrito"),
    path("caja/", CajaPage.as_view(), name="caja"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("perfil/", profile_view, name="profile"),
    path("perfil/editar/", profile_update_view, name="profile_edit"),

    # Recuperación de contraseña
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="register_login/password_reset.html"
    ), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="register_login/password_reset_done.html"
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="register_login/password_reset_confirm.html"
    ), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="register_login/password_reset_complete.html"
    ), name="password_reset_complete"),

    # Compatibilidad con archivos .html antiguos
    path("index.html", RedirectView.as_view(pattern_name="store:home", permanent=False)),
    path("register_login/login.html", RedirectView.as_view(pattern_name="store:login", permanent=False)),
    path("register_login/registro.html", RedirectView.as_view(pattern_name="store:register", permanent=False)),
    path("carrito/carrito.html", RedirectView.as_view(pattern_name="store:carrito", permanent=False)),
    path("caja/caja.html", RedirectView.as_view(pattern_name="store:caja", permanent=False)),
]

