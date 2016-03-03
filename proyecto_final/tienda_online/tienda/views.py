from django.shortcuts import render
from tienda.models import articulos,comentarios,pedido,linea,usuarios
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

# Create your views here.

def indice(request):
   lista_articulos = articulos.objects.all()
   return render(request, 'tienda/index.html', {'lista_articulos': lista_articulos })

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "tienda/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
		form = AuthenticationForm()
	return render(request,'tienda/login.html', {'form': form,})

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")
