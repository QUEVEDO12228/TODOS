# --> Clase que representa un producto
class Producto:
	def __init__(self, id_producto, nombre, precio):
		self.id = id_producto
		self.nombre = nombre
		self.precio = precio
# --> Clase que maneja todas las operaciones del sistema
class SistemaProductos:
	def __init__(self):
		self.productos = []
	# --> Metodo para buscar un producto.
	def buscar_producto(self, id_producto)
		for p in self.productos:
			if p.id == id_productos:
				return p			
		return None
	
	# --> Metodo Create -> Crear producto.
	def crear_producto(self, id_producto, nombre, precio):
		if self.buscar_producto(id_producto) is not None:
			print("Error, ya existe un producto con ese id")
			return 
		producto = Producto(id_producto, nombre, precio)
		self.productos.append(producto)
		print("Producto creado exitosamente")
	# --> Metodo Read -> Listar Producto
	def listar_producto(self):
		if len(self.productos) == 0:
			print("No hay productos registrados")
			return
		print("\n Lista de productos")
		for p in self.productos:
			print("|ID: ", p.id, "|Nombre: " p.nombre "|Precio: " p.precio)
	
	# --> Metodo Update -> Actualizar Producto
	def actualizar_producto(self, id_producto, nuevo_nombre, nuevo precio):
		producto = self.buscar_producto(id_producto)
	
		if producto is None:
			print("Producto no encontrado")
			return
		producto.nombre = nuevo_nombre
		producto.precio = nuevo_precio
		print("Producto actualizado correctamente")

	# --> Metodo Delete -> Eliminar producto
	def eliminar_producto(self, id_producto):
		producto = self.buscar_producto(id_producto):
		if producto is None:
			print("Producto no encontrado")
			return
		self.productos.remove(producto)
		print("Producto eliminado con exito")

# Función Principal Del Sistema.
def main()
	sistema = SistemaProductos()
	
	while True:
		print("\n Sistema de Productos")
		print("1. Crear Producto ")
		print("2. Listar Producto ")
		print("3. Actulizar Producto ")
		print("4. Eliminar producto ")
		print("5. Salir ")
		opcion = input("Seleccione una opción")
		
		# Crear Producto
		if opcion == "1":
			id_producto = input("ID: ")
			nombre = input("Nombre: ")
			precio = float(input("Precio: "))
			sistema.crear_producto(id_producto, nombre, precio)
			print("\n Presione Enter para continuar")

		# Listar Producto
		elif opcion == "2":
			sistema.listar_productos()
			print("\n Presione Enter para continuar")

		# Actualizar Producto
		elif opcion == "3":
			id_producto = input("ID: ")
			nombre = input("Nuevo Nombre: ")
			precio = float(input("Nuevo Precio: "))
			sistema.actualizar_producto(id_producto, nombre, precio)
			print("\n Presione Enter para continuar") 
		
		# Eliminar Producto
		elif opcion == "4":
			id_producto = input("ID del producto a eliminar: ")
			sistema.eliminar_producto(id_producto)
			input("\n Presione Enter para continuar")

		# Salir el sistema
		elif opcion == "5":
			print("Saliendo del sistema")
			break
		else:
			print("Opción Invalida")
			input("\n Presione Enter para continuar")
# Ejecutar el programa
main()
			