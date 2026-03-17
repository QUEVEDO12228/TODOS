# Desarrolle un programa en Python que permita gestionar la información de una institución educativa mediante 
# la implementación de dos módulos con operaciones CRUD completas (Crear, Listar, Actualizar y Eliminar). 
# El sistema debe manejar la gestión de estudiantes y la gestión de cursos utilizando Programación Orientada a Objetos.
# Para el módulo de estudiantes, se debe crear una clase llamada Estudiante que contenga los atributos id, nombre y edad. 
# El sistema debe permitir registrar estudiantes, listar todos los estudiantes, buscar un estudiante por su ID, 
# actualizar su información y eliminarlo del sistema.
# Para el módulo de cursos, se debe crear una clase llamada Curso que contenga los atributos id y nombre del curso. 
# El sistema debe permitir registrar cursos, listar todos los cursos, buscar un curso por su ID, actualizar su información y eliminarlo del sistema.
# Se debe crear una clase adicional llamada Sistema que se encargue de gestionar ambos módulos utilizando listas para almacenar la información. 
# Además, se debe implementar un menú interactivo que permita al usuario seleccionar las diferentes opciones para operar sobre estudiantes y cursos.
# El sistema debe validar que no se repitan los IDs al momento de registrar nuevos datos y 
# debe mostrar mensajes adecuados cuando un registro no exista al intentar consultarlo, actualizarlo o eliminarlo. 
# Se deben aplicar buenas prácticas de programación, mantener el código organizado y utilizar nombres claros en variables y métodos.

# Clase Estudiante
class Estudiante:
    def __init__(self, id_estudiante, nombre, edad):
        self.id = id_estudiante
        self.nombre = nombre
        self.edad = edad
# Clase Curso
class Curso:
    def __init__(self, id_curso, nombre):
        self.id = id_curso
        self.nombre = nombre
# Sistema que maneja los CRUD
class Sistema:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []
    # =========================
    # CRUD ESTUDIANTES
    # =========================
    def buscar_estudiante(self, id_estudiante):
        for e in self.estudiantes:
            if e.id == id_estudiante:
                return e
        return None
    def crear_estudiante(self, id_estudiante, nombre, edad):
        if self.buscar_estudiante(id_estudiante):
            print("Error: el estudiante ya existe")
            return
        self.estudiantes.append(Estudiante(id_estudiante, nombre, edad))
        print("Estudiante creado con éxito")
    def listar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes")
            return
        for e in self.estudiantes:
            print(f"ID: {e.id} | Nombre: {e.nombre} | Edad: {e.edad}")
    def actualizar_estudiante(self, id_estudiante, nombre, edad):
        e = self.buscar_estudiante(id_estudiante)
        if not e:
            print("Estudiante no encontrado")
            return
        e.nombre = nombre
        e.edad = edad
        print("Estudiante actualizado")
    def eliminar_estudiante(self, id_estudiante):
        e = self.buscar_estudiante(id_estudiante)
        if not e:
            print("Estudiante no encontrado")
            return
        self.estudiantes.remove(e)
        print("Estudiante eliminado")
    # =========================
    # CRUD CURSOS
    # =========================
    def buscar_curso(self, id_curso):
        for c in self.cursos:
            if c.id == id_curso:
                return c
        return None
    def crear_curso(self, id_curso, nombre):
        if self.buscar_curso(id_curso):
            print("Error: el curso ya existe")
            return
        self.cursos.append(Curso(id_curso, nombre))
        print("Curso creado con éxito")
    def listar_cursos(self):
        if not self.cursos:
            print("No hay cursos")
            return
        for c in self.cursos:
            print(f"ID: {c.id} | Nombre: {c.nombre}")
    def actualizar_curso(self, id_curso, nombre):
        c = self.buscar_curso(id_curso)
        if not c:
            print("Curso no encontrado")
            return
        c.nombre = nombre
        print("Curso actualizado")
    def eliminar_curso(self, id_curso):
        c = self.buscar_curso(id_curso)
        if not c:
            print("Curso no encontrado")
            return
        self.cursos.remove(c)
        print("Curso eliminado")
# =========================
# MENÚ PRINCIPAL
# =========================
def main():
    sistema = Sistema()

    while True:
        print("\n===== SISTEMA =====")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Crear curso")
        print("6. Listar cursos")
        print("7. Actualizar curso")
        print("8. Eliminar curso")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            sistema.crear_estudiante(id, nombre, edad)

        elif opcion == "2":
            sistema.listar_estudiantes()

        elif opcion == "3":
            id = input("ID: ")
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            sistema.actualizar_estudiante(id, nombre, edad)

        elif opcion == "4":
            id = input("ID: ")
            sistema.eliminar_estudiante(id)

        elif opcion == "5":
            id = input("ID curso: ")
            nombre = input("Nombre curso: ")
            sistema.crear_curso(id, nombre)

        elif opcion == "6":
            sistema.listar_cursos()

        elif opcion == "7":
            id = input("ID curso: ")
            nombre = input("Nuevo nombre: ")
            sistema.actualizar_curso(id, nombre)

        elif opcion == "8":
            id = input("ID curso: ")
            sistema.eliminar_curso(id)

        elif opcion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


main()