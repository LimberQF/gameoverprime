from django.urls import path
from .views import (
    HomePage, CategoryListPage, CategoryDetailPage,
    CarritoPage, CajaPage, LoginPage, RegisterPage
)

app_name = "store"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("categorias/", CategoryListPage.as_view(), name="category"),
    path("categorias/<slug:slug>/", CategoryDetailPage.as_view(), name="category_detail"),
    path("carrito/", CarritoPage.as_view(), name="carrito"),
    path("caja/", CajaPage.as_view(), name="caja"),
    path("login/", LoginPage.as_view(), name="login"),
    path("register/", RegisterPage.as_view(), name="register"),
]