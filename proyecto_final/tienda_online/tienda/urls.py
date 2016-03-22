from django.conf.urls import url
from tienda import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
   url(r'^registro$', views.registro, name='registro'),
   url(r'^login$', views.loginpage, name='login'),
   url(r'^logout$', views.logoutpage, name='logout'),
   url(r'^tipo/(?P<tipo_nombre>\w+)/$',views.tipo, name='tipo'),
   url(r'^especificaciones/(?P<articulo_id>\d+)/$',views.especificaciones, name='especificaciones'),
   url(r'^addcart$',views.addcart,name='addcart'),
   url(r'^carrito$',views.carrito,name='carrito'),
   url(r'^delcart/(?P<articulo_id>\d+)/$',views.delcart,name='delcart'),
   url(r'^comprar$',views.comprar,name='comprar'),
   url(r'^pedido/(?P<pedido_id>\d+)/$',views.pedido,name='pedido'),	
]
