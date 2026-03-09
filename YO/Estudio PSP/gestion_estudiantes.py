/* Desarrolle un programa en python, Cree una clase llamada Estudiante que contenga los atrubutos id, nombre, edad. Ademas, cree una clase llamada SistemaEstudiantes que se encargue
de gestionar a todos los estudiantes dentro del sistema utilizando una lista. crear estudiante, listar estudiante, actualizar estudiante, eliminar estudiante y debe
tener en cuenta el menu de opciones */
# Clase que simula un estudiante
class Estudiantes:
	def __init__(self, id_estudiante, nombre, edad)
		self.id = id_estudiante
		self.nombre = nombre
		self.edad = edad
# Clase que gestiona las operaciones crud de los estudiantes. 
class SistemaEstudiantes:
	def __init__(self)
		self.estudiante = []
	#--> Metodo buscar estudiante
	def buscar_estudiante(self, id_estudiante)
		for e in self.productos(id_estudiante)
			if e.id == id_estudiante
			return e
		return None
	#--> Metodo Crear Estudiante
	def crear_estudiante(self, id_estudiante, nombre, edad)
		if self.buscar_estudiante(id_estudiante) is not None:
			print("Error, ya existe ese id")
			return
		estudiante = Estudiante(id_estudiante, nombre, edad)
		self.estudiantes.append(estudiante)
		print("Estudiante creado con exito")
	
	#--> Metodo Listar estudiante
	def listar_estudiantes(self)
		if len(self.estudiantes) == 0:
			print("No hay estudiantes registrados")
			return
		for e in estudiantes:
			print("ID: ", e.id, "Nombre: ", e.nombre, "Edad: ", e.edad)
			
	#--> Metodo Actualizar Estudiante
	def actualizar_estudiante(id_estudiante, nuevo_nombre, nueva_edad)
		estudiante = self.buscar_estudiante(id_estudiante)
		if estudiante is None:
			print("Estudiante no encontrado")
			return
		estudiante.nombre = nuevo_nombre
		estudiante.edad = nueva_edad
		print("Estudiante actualizado con exito")

	#--> Metodo Eliminar Estudiante
	def eliminar_estudiante(self, id_estudiante)
|		estudiante = self.buscar_estudiante(id_estudiante)
		if estudiante is None:
			print("Estudiante no encontrado")
		self.estudiantes.remove(id_estudiante)
		print("Estudiante eliminado con exito")

# Funcion principal
def main()
	sistema = SistemaEstudiante()
	
	while True:
		print("Sistema de gestión de estudiantes")
		print("1. Crear estudiante ")
		print("2. Listar estudiante ")
		print("3. Actualizar Estudiante")
		print("4. Eliminar Estudiante ")
		print("5. Salir ")

		opcion = input("Seleccione una opcion: ")
		
		# Crear Estudiante
		if opcion == "1":
			id_estudiante = input("ID: ")
			nombre = input("Nombre: ")
			edad = int(input("Edad: "))
			sistema.crear_estudiante(id_estudiante, nombre, edad)
			input("ENTER")
		
		# Listar Estudiantes
		if opcion == "2":
			sistema.listar_estudiantes()
			input("ENTER")

		# Actualizar Estudiantes
		if opcion == "3":
			id_Estudiante = input("ID: ")
			nombre = input("Nuevo Nombre: ")
			edad = int(input("Nueva edad: ")
			sistema.actualizar_estudiante(id_Estudiante, nombre, edad) 
			input("ENTER")

		# Eliminar estudiante
		if opcion == "4":
			id_estudiante = input("ID estudiante a eliminar: ")
			sistema.eliminar_estudiante(id_estudiante)
			input("ENTER")

		if opcion == "5":
			print("Saliendo...") 			
			break	
		else:
			print("Opción Invalida")
			input("Enter")
main()