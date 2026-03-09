# Clase que representa un vehículo
class Vehiculo:
    # Constructor de la clase Vehiculo
    # Se ejecuta automáticamente cuando se crea un objeto Vehiculo
    def __init__(self, placa, marca, modelo, año, precio):
        self.placa = placa     # Guarda la placa del vehículo
        self.marca = marca     # Guarda la marca (Toyota, Chevrolet, etc.)
        self.modelo = modelo   # Guarda el modelo
        self.año = año         # Guarda el año de fabricación
        self.precio = precio   # Guarda el precio del vehículo


# Clase que gestiona el CRUD
# CRUD significa: Crear, Leer, Actualizar y Eliminar
class SistemaVehiculos:

    # Constructor de la clase
    def __init__(self):
        self.vehiculos = []  # Lista donde se almacenarán todos los vehículos


    # Buscar vehículo por placa
    def buscar_vehiculo(self, placa):

        # Recorre todos los vehículos de la lista
        for v in self.vehiculos:

            # Si encuentra un vehículo con la misma placa
            if v.placa == placa:
                return v  # devuelve ese vehículo

        # Si no encuentra ninguno devuelve None
        return None


    # Crear vehículo
    def crear_vehiculo(self, placa, marca, modelo, año, precio):

        # Verifica si ya existe un vehículo con esa placa
        if self.buscar_vehiculo(placa) is not None:
            print("Error: la placa ya existe")
            return

        # Valida que la marca no esté vacía
        if marca == "":
            print("Error: la marca no puede estar vacía")
            return

        # Valida que el año esté dentro del rango permitido
        if año < 1990 or año > 2025:
            print("Error: el año debe estar entre 1990 y 2025")
            return

        # Valida que el precio sea mayor que 0
        if precio <= 0:
            print("Error: el precio debe ser mayor que 0")
            return

        # Crea un objeto Vehiculo con los datos ingresados
        vehiculo = Vehiculo(placa, marca, modelo, año, precio)

        # Agrega el vehículo a la lista
        self.vehiculos.append(vehiculo)

        print("Vehículo registrado correctamente")


    # Listar vehículos
    def listar_vehiculos(self):

        # Si la lista está vacía
        if len(self.vehiculos) == 0:
            print("No hay vehículos registrados")
            return

        # Recorre la lista y muestra los datos de cada vehículo
        for v in self.vehiculos:
            print("Placa:", v.placa, 
                  "| Marca:", v.marca, 
                  "| Modelo:", v.modelo, 
                  "| Año:", v.año, 
                  "| Precio:", v.precio)


    # Actualizar vehículo
    def actualizar_vehiculo(self, placa, nueva_marca, nuevo_modelo, nuevo_año, nuevo_precio):

        # Busca el vehículo por placa
        vehiculo = self.buscar_vehiculo(placa)

        # Si no existe
        if vehiculo is None:
            print("Vehículo no encontrado")
            return

        # Validaciones
        if nueva_marca == "":
            print("Error: la marca no puede estar vacía")
            return

        if nuevo_año < 1990 or nuevo_año > 2025:
            print("Error: el año debe estar entre 1990 y 2025")
            return

        if nuevo_precio <= 0:
            print("Error: el precio debe ser mayor que 0")
            return

        # Actualiza los datos del vehículo
        vehiculo.marca = nueva_marca
        vehiculo.modelo = nuevo_modelo
        vehiculo.año = nuevo_año
        vehiculo.precio = nuevo_precio

        print("Vehículo actualizado correctamente")


    # Eliminar vehículo
    def eliminar_vehiculo(self, placa):

        # Busca el vehículo
        vehiculo = self.buscar_vehiculo(placa)

        # Si no existe
        if vehiculo is None:
            print("Vehículo no encontrado")
            return

        # Lo elimina de la lista
        self.vehiculos.remove(vehiculo)

        print("Vehículo eliminado correctamente")


# Función principal del programa
def main():

    # Se crea el sistema que manejará los vehículos
    sistema = SistemaVehiculos()

    # Bucle infinito para mostrar el menú siempre
    while True:

        # Menú del sistema
        print("\n===== SISTEMA DE VEHÍCULOS =====")
        print("1. Registrar vehículo")
        print("2. Listar vehículos")
        print("3. Actualizar vehículo")
        print("4. Eliminar vehículo")
        print("5. Salir")

        # Se pide una opción al usuario
        opcion = input("Seleccione una opción: ")

        # Crear vehículo
        if opcion == "1":

            # Se piden los datos
            placa = input("Placa: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")

            # Convertimos el input a número
            año = int(input("Año: "))
            precio = float(input("Precio: "))

            # Se llama al método para crear el vehículo
            sistema.crear_vehiculo(placa, marca, modelo, año, precio)

            input("\nPresione ENTER para continuar...")


        # Listar vehículos
        elif opcion == "2":

            sistema.listar_vehiculos()

            input("\nPresione ENTER para continuar...")


        # Actualizar vehículo
        elif opcion == "3":

            placa = input("Placa del vehículo: ")
            marca = input("Nueva marca: ")
            modelo = input("Nuevo modelo: ")
            año = int(input("Nuevo año: "))
            precio = float(input("Nuevo precio: "))

            sistema.actualizar_vehiculo(placa, marca, modelo, año, precio)

            input("\nPresione ENTER para continuar...")


        # Eliminar vehículo
        elif opcion == "4":

            placa = input("Placa del vehículo a eliminar: ")

            sistema.eliminar_vehiculo(placa)

            input("\nPresione ENTER para continuar...")


        # Salir del programa
        elif opcion == "5":

            print("Saliendo del sistema...")
            break


        # Si el usuario escribe una opción incorrecta
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar...")


# Ejecuta el programa
main()