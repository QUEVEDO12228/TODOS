class Vehiculo:
	def __init__(self, placa, marca, modelo, año, precio):
		self.placa = placa
		self.marca = marca
		self.modelo = modelo
		self.año = año
		self.precio = precio
class SistemaVehiculos:
    def __init__(self):
        self.vehiculos = []
    def buscar_vehiculo(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                return v
        return None
    def crear_vehiculo(self, placa, marca, modelo, año, precio):
        if self.buscar_vehiculo(placa) is not None:
            print("Placa ya existe")
            return
        if len(placa) != 6:
            print("debe ser de 6 digitos")
            return
        if not placa[:3].isalpha():
            print("xxx123")	
            return
        if not placa[3:].isdigit():
            print("xxx123")
            return
        if marca == "":
            print(" no vacia ")
            return
        if año < 1990 or año > 2025:
            print(" 1990 a 2025 ")
            return
        if precio <= 0:
            print("> 0 ")
            return
        vehiculo = Vehiculo(placa, marca, modelo, año, precio)
        self.vehiculos.append(vehiculo)
        print("vehiculos")

    def listar_vehiculo(self):
        if len(self.vehiculos) == 0:
            print("No hay vehiculos")
            return
        for v in self.vehiculos:
            print("PLACA: ", v.placa, "MARCA: ", v.marca, "MODELO: ", v.modelo, "AÑO: ", v.año, "PRECIO: ", v.precio)

    def actualizar_vehiculo(self, placa, nueva_marca, nuevo_modelo, nuevo_año, nuevo_precio):
        vehiculo = self.buscar_vahiculo(placa)
        if vehiculo is None:
            print("No hay vehiculo")
            return
        if nueva_marca == "":
            print("Marca vacia")
            return
        if nuevo_año < 1990 or nuevo_año > 2025:
            print("1990 a 2025")
            return
        if nuevo_precio <= 0:
            print("Menor q 0")
            return
        vehiculo.marca = nueva_marca
        vehiculo.modelo = nuevo_modelo
        vehiculo.año = nuevo_año
        vehiculo.precio = nuevo_precio 

        print("actualizado")


    def eliminar_vehiculo(self, placa):
        vehiculo = self.buscar_vehiculo(placa)
        if vehiculo is None:
            print("No hay vehiculo")
            return
        self.vehiculos.remove(vehiculo)
        print("eliminado")

def main():
	sistema =  SistemaVehiculos()
	
	while True:
		print("GESTIÓN VEHÍCULOS")
		print("1. CREAR VEHÍCULO")
		print("2. LISTAR VEHÍCULOS")
		print("3. ACTUALIZAR VEHÍCULO")
		print("4. ELIMINAR VEHÍCULO")
		print("5. SALIR")
		opcion = input("seleccione una opcion: ")
		
		if opcion == "1":
			placa = input("PLACA: ")
			marca = input("MARCA: ")
			modelo = input("MODELO: ")
			año = int(input("AÑO: "))
			precio = float(input("PRECIO: "))
			sistema.crear_vehiculo(placa, marca, modelo, año, precio)
			input()

		if opcion == "2":
			sistema.listar_vehiculos()
			input()
		
		if opcion == "3":
			placa = input("PLACA: ")
			marca = input("MARCA: ")
			modelo = input("MODELO: ")
			año = int(input("AÑO: "))
			precio = float(input("PRECIO: "))
			sistema.actualizar_vehiculo(placa, marca, modelo, año, precio)
			input()

		if opcion == "4":
			placa = input("PLACA A ELIMINAR: ")
			sistema.eliminar_vehiculo(placa)
			input()
		
		if opcion == "5":
			print("Saliendo...")
			break
			
		else:
			print("Opción Invalida")
			input()

main()