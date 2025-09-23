# GameOverPrime 🎮 – Proyecto Web Grupo 7

Aplicación web desarrollada con Django y Oracle XE para la gestión de una tienda de videojuegos. Incluye autenticación, edición de perfil, carrito de compras, y validaciones de formularios.

## Tecnologías utilizadas

- Django 4.x
- Oracle XE 18c
- HTML, CSS, Bootstrap 5, JavaScript
- PowerShell (Windows)
- Git y GitHub

## Funcionalidades principales

- Inicio de sesión y registro de usuarios
- Recuperación y cambio de contraseña con validaciones
- Edición de perfil con validación de edad mínima
- Carrito de compras y caja
- Interfaz responsiva adaptada a escritorio, tablet y móvil
- Seguridad de acceso por roles

## Instalación

1. Crear entorno virtual y activar
2. Instalar dependencias con `pip install -r requirements.txt`
3. Configurar Oracle XE y ejecutar el script SQL
4. Ejecutar el servidor con `python manage.py runserver`

## Entregables incluidos

- Código fuente completo
- Script de base de datos (`oracle_setup.sql`)

## Descripcion del MER
El modelo entidad-relación (MER) de GameOverPrime representa la estructura lógica de la base de datos utilizada en la aplicación web. Está normalizado hasta tercera forma normal (3FN) y contempla las siguientes entidades principales:
- Usuario: almacena credenciales y datos básicos de acceso.
- Perfil: extiende la información del usuario con datos personales y rol asignado.
- Rol: define los tipos de usuario (cliente, administrador).
- Producto: contiene información sobre los videojuegos disponibles.
- CarritoItem: representa los productos seleccionados por el usuario antes de la compra.
- Orden: registra compras confirmadas por el usuario.
- DetalleOrden: vincula productos con cada orden, incluyendo cantidad y precio.
Todas las relaciones están definidas mediante claves foráneas, y el modelo permite trazabilidad completa del flujo de compra, desde la selección de productos hasta el registro de órdenes. El MER fue diseñado y exportado desde Oracle DataModeler, y se incluye como imagen (PNG) en la entrega.
