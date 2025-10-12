# GameOverPrime 🎮 – Proyecto Web Grupo 7

**Repositorio principal:** https://github.com/LimberQF/gameoverprime  
**Respaldo:** https://github.com/Engg13/GameOverPrime.Respaldo

## 📌 Descripción

GameOverPrime es una tienda de videojuegos desarrollada con Django y Oracle, que integra seguridad JWT, consumo de API externa y visualización dinámica en el frontend. Este proyecto cumple con todos los criterios de la rúbrica académica, incluyendo trazabilidad, documentación y validación técnica.

## 🧱 Estructura del proyecto

- `/backend/` → Proyecto Django con configuración Oracle y JWT
- `/frontend/` → Archivos HTML, CSS y JS con consumo de APIs
- `/scripts/` → PowerShell y SQL para pruebas, truncado y evidencias
- `/docs/` → Documentación técnica, rúbrica y tablas de validación



## 🔐 Seguridad JWT

- Implementación con `djangorestframework-simplejwt`
- Rutas activas:
  - `/api/token/` → generación de token
  - `/api/token/refresh/` → renovación
- Protección de rutas con `IsAuthenticated`
- Validación en Postman: acceso restringido sin token (`401`), acceso autorizado con token (`200 OK`)

## 🌐 Consumo de API externa

- API integrada: [NewsAPI](https://newsapi.org)
- Ruta: `/api/noticias/`
- Visualización en frontend: sección “Noticias Gamer”
- Validación de respuesta en español

## 🔁 Consumo de API propia

- Rutas consumidas desde el frontend:
  - `/api/productos/`
  - `/api/categorias/`
- Uso de `fetch()` en `index.html`
- Visualización dinámica con Bootstrap

## 🗃️ Base de datos Oracle

- Conexión validada con Oracle
- Operaciones CRUD completas:
  - Crear, leer, actualizar y eliminar productos y categorías
- Validación desde frontend y Postman

## 📄 Documentación y trazabilidad

- `README.md` con estructura, rutas, seguridad y APIs
- Commits comentados y organizados por rama
- Evidencia técnica y académica para cada punto de la rúbrica

## 🎥 Video de presentación

- En elaboración con participación de todos los integrantes
- Se abordarán todos los puntos solicitados por la rúbrica

## 📊 Cumplimiento de rúbrica

| Criterio                         | Evidencia técnica                         | Validación |
|----------------------------------|-------------------------------------------|------------|
| Seguridad JWT                    | Rutas `/api/token/`, Postman, `IsAuthenticated` | ✅         |
| API externa                      | `/api/noticias/`, integración con NewsAPI | ✅         |
| API propia                       | `/api/productos/`, `/api/categorias/`, consumo con `fetch()` | ✅         |
| Oracle CRUD                      | Tablas `productos` y `categorias`, validación desde frontend y Postman | ✅         |
| Documentación                    | `README.md`, commits comentados y organizados | ✅         |
| Frontend dinámico                | Bootstrap, visualización con `fetch()` en `index.html` | ✅         |
