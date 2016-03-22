from django import forms
from tienda.models import comentarios
from tienda.models import pedido

class comentariosForm(forms.ModelForm):

	class Meta:
		model = comentarios
		fields = ('comentario',)

class pedidosForm(forms.ModelForm):

	class Meta:
		model = pedido
		fields = ('fecha_pedido','fecha_entrega','direccion_entrega')

