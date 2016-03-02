from django.contrib import admin
from tienda.models import articulos
from tienda.models import comentarios
from tienda.models import pedido
from tienda.models import linea
from tienda.models import usuarios

# Register your models here.

admin.site.register(articulos)
admin.site.register(comentarios)
admin.site.register(pedido)
admin.site.register(linea)
admin.site.register(usuarios)

