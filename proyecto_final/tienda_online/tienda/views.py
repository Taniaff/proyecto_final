from django.shortcuts import render
from tienda.models import articulos,comentarios,pedido,linea,usuarios
# Create your views here.
def indice(request):
   lista_articulos = articulos.objects.all()
   return render(request, 'tienda/index.html', {'lista_articulos': lista_articulos })
