from django.conf.urls import url
from tienda import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
		
]
