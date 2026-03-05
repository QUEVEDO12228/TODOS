from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.db import transaction


# Create your views here.

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#el usuario debe estar autenticado para crear el producto
@login_required
# Vista para crear el producto
def crear_producto(request):

    #procesar el formulario (Si se envía)
    if request.method == 'POST':
        #Se capturan los datos del producto y la imagen
        form = ProductoForm(request.POST, request.FILES)

        #se valida si el formulario es valido
        if form.is_valid():
            #si cumple, se guarda en l bd con el método save de Django
            form.save()
            #redirige a la lista de productos
            return redirect('lista_productos')

    #si el metodo es GET muestra el formulario vacío
    else:
        form = ProductoForm()

    #se carga el formulario para crear el producto
    return render(request,'productos/crear_producto.html',{'form':form})


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#el usuario debe estar autenticado para listar el producto
@login_required
#Vista para listar los productos Tiene filtro para mostrar productos: Habilitados, Deshabilitados, Todos
def lista_productos(request):
    #busca el filtro seleccionado, si no se selecciona por defecto es mostrar los productos activos
    filtro = request.GET.get('filtro', 'activos')

    #filtro si el producto se encuentra deshabilitado
    if filtro == 'deshabilitados':
        #muestra todos los productos que en la bd que se encuentren con estado deshabilitado
        productos = Producto.objects.filter(activo=False)

    #filtro para mostrar todos los productos
    elif filtro == 'todos':
        #muestra todos los productos que estan en la bd
        productos = Producto.objects.all()

    #filtro si el producto se encuentra habilitado
    else:
        #muestra todos los productos que en la bd que se encuentren con estado habilitado
        productos = Producto.objects.filter(activo=True)

    '''se crea un diccionario para enviar productos (que es la lista filtrada) y filtro (el filtro
    que se haya seleccionado)'''
    context = {'productos': productos, 'filtro': filtro}

    '''muestra el HTML con el context (carga la página con los productos y el filtro)'''
    return render(request, 'productos/lista_productos.html', context)


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Vista basada en clases
#Vista para mostrar el detalle de un producto, con la vista DetailView que tiene Django
class ProductoDetalleView(DetailView):
    #se trabaja con el model Producto para acceder a los campos
    model = Producto
    #archivo HTML que se usa para mostrar el detalle del producto
    template_name = 'productos/detalle_producto.html'
    #nombre del objeto para ser usado en el HTML
    context_object_name = 'producto'

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Vista basada en clases
#Vista para actualizar un producto, con la vista UpdateView que tiene Django
class ProductoUpdateView(UpdateView):
     #se trabaja con el model Producto para acceder a los campos
    model = Producto
    #utiliza el formulario ProductoForm que tiene forms
    form_class = ProductoForm
    #archivo HTML que se usa para actualizar el producto
    template_name = 'productos/crear_producto.html'
    #despues de guardar (lo hace la vista UpdateView) redirige a la vista lista de productos
    success_url = reverse_lazy('lista_productos')

    
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Vista para cambiar el estado de los productos
# se recibe la llave primaria del producto al que se desea cambiar el estdado
def cambiar_estado_producto(request, pk):

    '''get_object_or_404 busca en la bd el producto que llega como ID por la URL. Si el producto 
    no existe muestra error 404'''
    #Producto es el producto al que se le desea cambiar el estado
    producto = get_object_or_404(Producto, pk=pk)
    #cambia el estado actual del producto    
    producto.activo = not producto.activo
    #utilizamos el método save de Django para actualizar el estado del producto
    producto.save()
    #carga la pagina con la lista de productos
    return redirect('lista_productos')


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#el usuario debe estar autenticado para listar el producto
@login_required
#Vista para buscar los productos
def buscar_productos_ajax(request):
    #q recibe el producto que se desea buscar (lo que el usuario va escribiendo)
    # '' si no se selecciona esta vacío
    q = request.GET.get('q', '')
    #verifica si tiene filtro (todos, activo, inactivo) si no tiene filtro por defecto es activo
    filtro = request.GET.get('filtro', 'activos')

    '''nombre__icontains (busca el nombre que se va ingresando sin importar mayusculas o 
    minusculas)'''

    #si el filtro se encuentra en deshabilitados
    if filtro == 'deshabilitados':
        #busca lo que se va ingresando dentro de los productos que tengan el estado deshabilitados
        productos = Producto.objects.filter(activo=False, nombre__icontains=q)

    #si el filtro se encuentra en todos
    elif filtro == 'todos':
        #busca lo que se va ingresando dentro de todos los productos
        productos = Producto.objects.filter(nombre__icontains=q)

    #si el filtro se encuentra en activos
    else:
        #busca lo que se va ingresando dentro de los productos que tengan el estado habilitados
        productos = Producto.objects.filter(activo=True, nombre__icontains=q)

    #se carga como tipo texto la información de cada producto 
    html = render_to_string('productos/tarjetas_lista_productos.html', {'productos': productos,'filtro': filtro}, request=request)

    #se utiliza el AJAX para que solo procese datos pequeños para ir actualizando la pagina. Devuelve el producto que cumple
    #con la información que se va digitando y va actualizando la sección de la página. Es decir permite realizar el proceso
    #actualizando la pagina de forma automatica (no hay que actualizar con F5 la pagina para ver los resultados)
    return JsonResponse({'html': html})


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#solo recibe metodo POST
@require_POST
#el usuario debe estar autenticado para listar el producto
@login_required
#vista para actualizar el estado del producto de forma automatica (sin actualizar la pagina)
def toggle_producto(request, pk):
    '''get_object_or_404 busca en la bd el producto que llega como ID por la URL. Si el producto 
    no existe muestra error 404'''
    #Producto es el producto al que se le desea cambiar el estado
    producto = get_object_or_404(Producto, pk=pk)
    #cambia el estado actual del producto  
    producto.activo = not producto.activo
    #utilizamos el método save de Django para actualizar el estado del producto
    producto.save()

    #indica si el cambio de estado fue realizado e indica el nuevo estado del producto
    return JsonResponse({'success': True, 'nuevo_estado': producto.activo})

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#el usuario debe estar autenticado para listar el producto
@login_required
#Se ejecuta el proceso completo para guardar. Si algo falla no guarda (Protección de datos)
@transaction.atomic
#vista para agregar productos al carrito
def agregar_al_carrito(request, producto_id):
    '''get_object_or_404 busca en la bd el producto que llega como ID por la URL. Si el producto 
    no existe muestra error 404'''
    #Producto es el producto que se va a agregar al carrito
    producto = get_object_or_404(Producto, id=producto_id)

    #verifica que el stock no sea 0 o menor que cero
    if producto.stock <= 0:
        #carga el popup para indicar que el producto no tiene stock
        return JsonResponse({'error': 'Producto sin stock'}, status=400)

    #se verifica si el usuario tiene un carrito creado, si no lo tiene crea el carrito
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    #se verifica si el producto ya esta en el carrito si no esta lo agrega
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    #con un carrito creado
    if not creado:
        #se verifica que la cantidad solicitada no supere el stock del producto
        if item.cantidad + 1 > producto.stock:
            #carga un mensaje con el stock insuficiente
            return JsonResponse({'error': 'Stock insuficiente'}, status=400)

        #si no supera el stock se suma 1 a la cantidad
        item.cantidad += 1
    else:
        #si el producto no estaba en el carrito se agrega y se pone 1
        item.cantidad = 1

    #se guarda con el método save de Django
    item.save()

    #se suman los productos que se tengan en el carrito
    total_items = sum(i.cantidad for i in carrito.items.all())
    #actualiza el contador del carrito y permite visualizar si el producto fue agregado al carrito
    return JsonResponse({'success': True, 'total_items': total_items})