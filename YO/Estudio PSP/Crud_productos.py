# Clase que representa un producto
class Producto:

    def __init__(self, id_producto, nombre, precio):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio


# Clase que maneja todas las operaciones del sistema
class SistemaProductos:

    def __init__(self):
        self.productos = []

    # Método para buscar un producto por ID
    def buscar_producto(self, id_producto):

        for p in self.productos:
            if p.id == id_producto:
                return p

        return None


    # CREATE -> Crear producto
    def crear_producto(self, id_producto, nombre, precio):

        if self.buscar_producto(id_producto) is not None:
            print("Error: ya existe un producto con ese ID")
            return

        producto = Producto(id_producto, nombre, precio)
        self.productos.append(producto)

        print("Producto creado exitosamente")


    # READ -> Listar productos
    def listar_productos(self):

        if len(self.productos) == 0:
            print("No hay productos registrados")
            return

        print("\nLista de productos:")
        for p in self.productos:
            print("ID:", p.id, "| Nombre:", p.nombre, "| Precio:", p.precio)


    # UPDATE -> Actualizar producto
    def actualizar_producto(self, id_producto, nuevo_nombre, nuevo_precio):

        producto = self.buscar_producto(id_producto)

        if producto is None:
            print("Producto no encontrado")
            return

        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio

        print("Producto actualizado correctamente")


    # DELETE -> Eliminar producto
    def eliminar_producto(self, id_producto):

        producto = self.buscar_producto(id_producto)

        if producto is None:
            print("Producto no encontrado")
            return

        self.productos.remove(producto)
        print("Producto eliminado correctamente")


# Función principal del programa
def main():

    sistema = SistemaProductos()

    while True:

        print("\n===== SISTEMA DE PRODUCTOS =====")
        print("1. Crear Producto")
        print("2. Listar Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        # Crear producto
        if opcion == "1":

            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))

            sistema.crear_producto(id_producto, nombre, precio)
            input("\nPresione ENTER para continuar...")


        # Listar productos
        elif opcion == "2":

            sistema.listar_productos()
            input("\nPresione ENTER para continuar...")


        # Actualizar producto
        elif opcion == "3":

            id_producto = input("ID del producto: ")
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))

            sistema.actualizar_producto(id_producto, nombre, precio)
            input("\nPresione ENTER para continuar...")


        # Eliminar producto
        elif opcion == "4":

            id_producto = input("ID del producto a eliminar: ")
            sistema.eliminar_producto(id_producto)
            input("\nPresione ENTER para continuar...")


        # Salir
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar...")


# Ejecutar el programa
main()