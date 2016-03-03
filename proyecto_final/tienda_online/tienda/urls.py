from django.conf.urls import url
from tienda import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
   url(r'^registro$', views.registro, name='registro'),
   url(r'^login$', views.loginpage, name='login'),
   url(r'^logout$', views.logoutpage, name='logout'),	
]
