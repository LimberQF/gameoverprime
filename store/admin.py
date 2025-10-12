from django.contrib import admin
# from .models import Usuario, Rol

# admin.site.register(Usuario)
# admin.site.register(Rol)

from django.contrib import admin
from .models import Categoria, Producto

admin.site.register(Categoria)
admin.site.register(Producto)