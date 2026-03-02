from django.urls import path
from .views import *




urlpatterns = [
    path('crear/', crear_producto, name='crear_producto'),
    path('', lista_productos, name='lista_productos'),
    path('<int:pk>/', ProductoDetalleView.as_view(), name='detalle_producto'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('estado/<int:pk>/', cambiar_estado_producto, name='cambiar_estado_producto'),
    path('buscar_ajax/', buscar_productos_ajax, name='buscar_productos_ajax'),
    path('toggle/<int:pk>/', toggle_producto, name='toggle_producto'),

]
