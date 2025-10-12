from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from store.models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer
from rest_framework.permissions import IsAuthenticated

# API externa: Noticias Gamer desde NewsAPI
@api_view(['GET'])
def noticias_gamer(request):
    api_key = '06d3909b1ff2413eba3c37c7fcdc24cb'
    url = f'https://newsapi.org/v2/everything?q=videojuegos&language=es&sortBy=publishedAt&apiKey={api_key}'
    try:
        response = requests.get(url)
        data = response.json()
        return Response(data.get('articles', []))
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# API propia: Categorías
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# API propia: Productos
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # 🔐 Solo usuarios con token pueden acceder
