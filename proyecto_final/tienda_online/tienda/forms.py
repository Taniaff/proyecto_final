from django import forms
from tienda.models import comentarios

class comentariosForm(forms.ModelForm):

	class Meta:
		model = comentarios
		fields = ('comentario',)
