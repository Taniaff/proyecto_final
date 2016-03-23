from django.shortcuts import render
from tienda.models import articulos,comentarios,pedido,linea
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from tienda.forms import comentariosForm,pedidosForm

# Create your views here.

def indice(request):
   lista_articulos = articulos.objects.values('tipo').distinct()
   return render(request, 'tienda/index.html', {'lista_articulos': lista_articulos })

def tipo(request,tipo_nombre):
	lista_articulos = articulos.objects.filter(tipo=tipo_nombre)
	return render (request, 'tienda/articulos.html', {'lista_articulos': lista_articulos,'tipo_nombre':tipo_nombre})

def especificaciones(request, articulo_id):
	if request.method == 'POST':
		form = comentariosForm(request.POST)
		if form.is_valid():
			comentario = form.save()
			comentario.usuario = request.user
			articulo = get_object_or_404(articulos, pk = articulo_id)
			comentario.articulo = articulo
			comentario.save()
			return HttpResponseRedirect("/especificaciones/"+articulo_id)
	else:
		lista_comentarios = comentarios.objects.filter(articulo=articulo_id)
		form = comentariosForm()
		articulo = get_object_or_404(articulos, pk = articulo_id)
		return render (request, 'tienda/especificaciones.html', {'articulo':articulo, 'lista_comentarios':lista_comentarios, 'form':form})

def addcart(request):
	if not "cart" in request.session:
		request.session["cart"] = {}
	if not "cantidad" in request.session:
		request.session["cantidad"]=0
	cantidad = request.POST.get('cantidad', '')
	id_art = request.POST.get('id', '')
	if id_art in request.session["cart"]:
		request.session["cart"][id_art]	=int(request.session["cart"][id_art])+int(cantidad)
		request.session["cantidad"]=int(request.session["cantidad"])+int(cantidad)
	else:
		request.session["cart"][id_art]=cantidad
		request.session["cantidad"]=int(request.session["cantidad"])+int(cantidad)
	return HttpResponseRedirect("/especificaciones/"+id_art)

def carrito(request):
	carrito = []
	for key in request.session["cart"]:
		articulo = get_object_or_404(articulos, pk = key)
		cantidad = request.session["cart"][key]
		precio = int(cantidad)*articulo.precio
		item = [articulo,cantidad,precio]
		carrito.append(item)
	return render (request, 'tienda/carrito.html', {'carrito':carrito})

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


def delcart(request,articulo_id):
	cantidad = request.session["cart"][articulo_id]
	request.session["cantidad"]=int(request.session["cantidad"])-int(cantidad)
	request.session.modified = True
	del request.session["cart"][articulo_id]
	request.session.modified = True
	
	return HttpResponseRedirect("/carrito")

def comprar(request):
	if request.method == "POST":
		form = pedidosForm(request.POST)
		if form.is_valid():
			pedido_actual = form.save()
			pedido_actual.autor_pedido = request.user
			pedido_actual.save()
			for key in request.session["cart"]:
				articulo = get_object_or_404(articulos, pk = key)
				l = linea(cod_articulo=articulo,cantidad=request.session["cart"][key],cod_pedido=pedido_actual)
				l.save()	
			return HttpResponseRedirect("/pedido_nuevo/"+str(pedido_actual.id))
	else:
		form = pedidosForm()
	return render(request, 'tienda/pedidos.html', {'form': form})

def pedido_nuevo(request,pedido_id):
	lineas = linea.objects.filter(cod_pedido=pedido_id)
	pedido_actual = get_object_or_404(pedido, pk = pedido_id)
	carrito = []
	total=0
	for linea_actual in lineas:
		articulo = get_object_or_404(articulos, pk = str(linea_actual.cod_articulo.id))
		nombre = articulo.modelo
		precio_unitario = articulo.precio
		cantidad = linea_actual.cantidad	
		precio = int(linea_actual.cantidad)*articulo.precio
		total=total+precio
		item = [nombre,precio_unitario,cantidad,precio]
		carrito.append(item)
		print(carrito)
	return render(request, 'tienda/detalle_pedido.html', {'pedido_actual': pedido_actual,'carrito':carrito,'total':total,})	





