from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class articulos(models.Model):
	tipo = models.CharField(max_length=20)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	caracteristicas = models.CharField(max_length=200)
	precio = models.IntegerField()
	foto = models.ImageField(upload_to='tienda/static/media',null=True)
	def __str__(self):
		return '%s' % (self.modelo)

class comentarios(models.Model):
	comentario = models.CharField(max_length=200)
	articulo =  models.ForeignKey(articulos,null=True)
	usuario = models.ForeignKey (User,null=True)

class pedido(models.Model):
	fecha_pedido= models.DateField()
	fecha_entrega= models.DateField()
	direccion_entrega = models.CharField(max_length=50)
	autor_pedido = models.ForeignKey (User,null=True)

class linea(models.Model):
	cantidad = models.IntegerField()
	cod_pedido = models.ForeignKey(pedido)
	cod_articulo = models.ForeignKey(articulos)
	class Meta:
        	unique_together = (('cod_pedido', 'cod_articulo'),)

class usuarios(models.Model):
	nombre = models.CharField(max_length=20)
	apellidos = models.CharField(max_length=50)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=50)
	user = models.OneToOneField(User)
