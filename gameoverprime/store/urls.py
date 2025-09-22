from django.urls import path
from django.views.generic import RedirectView  
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

    # Compatibilidad con archivos .html antiguos 
    path("index.html", RedirectView.as_view(pattern_name="store:home", permanent=False)),
    path("register_login/login.html", RedirectView.as_view(pattern_name="store:login", permanent=False)),
    path("register_login/registro.html", RedirectView.as_view(pattern_name="store:register", permanent=False)),
    path("carrito/carrito.html", RedirectView.as_view(pattern_name="store:carrito", permanent=False)),
    path("caja/caja.html", RedirectView.as_view(pattern_name="store:caja", permanent=False)),
]

