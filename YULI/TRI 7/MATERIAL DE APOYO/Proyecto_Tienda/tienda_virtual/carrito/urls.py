from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_carrito'),
    path('actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('procesar/', views.procesar_pago, name='procesar_pago'),
	#path('exito/<int:pedido_id>/', views.pedido_exitoso, name='pedido_exitoso'),
]
