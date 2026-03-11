from datetime import datetime

class Persona: 
	def __init__(self, tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, telefono_fijo, correo_electronico, direccion):
		self.tipo_identificacion = tipo_identificacion
		self.numero_identificacion = numero_identificacion
		self.nombres_apellidos = nombres_apellidos
		self.rh_sanguineo = rh_sanguineo 
		self.telefono_celular = telefono_celular
		self.telefono_fijo = telefono_fijo
		self.correo_electronico = correo_electronico
		self.direccion = direccion
		self.estado = True

	def activar(self):
		self.estado = True

	def desactivar(self):
		self.estado = False


class Cliente(Persona):
	def __init__(self, tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, telefono_fijo, correo_electronico, direccion):
		super().__init__(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, telefono_fijo, correo_electronico, direccion)


class Personal(Persona):
	def __init__(self, tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, rol, correo_electronico, direccion):
		super().__init__(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, None, correo_electronico, direccion)
		self.rol = rol


class ProcedimientoAdministrativo:
	def __init__(self, codigo, nombre, descripcion):
		self.codigo = codigo
		self.nombre = nombre
		self.descripcion = descripcion


class ProcedimientoMedico:
	def __init__(self, codigo, nombre, descripcion):
		self.codigo = codigo
		self.nombre = nombre
		self.descripcion = descripcion


class HistorialMedico:
	def __init__(self, id_cliente, procedimiento, fecha):
		self.id_cliente = id_cliente
		self.procedimiento = procedimiento
		self.fecha = fecha


class SistemaClinica:
	def __init__(self):
		self.clientes = {}
		self.personal = {}
		self.procesos_administrativos = {}
		self.procesos_medicos = {}
		self.historial = []

	def validar_numero(self, texto):
		return texto.isdigit()

	def registrar_cliente(self):
		try:
			numero_identificacion = input("Numero de Identificación: ")
			if not self.validar_numero(numero_identificacion):
				print("Error: el número de identificación debe ser numérico.")
				return
			if numero_identificacion in self.clientes:
				print("Cliente ya existe.")
				return 

			tipo_identificacion = input("Tipo ID: ")
			nombres_apellidos = input("Nombre Completo: ")
			rh_sanguineo = input("RH Sanguineo: ")
			telefono_celular = input("Teléfono Celular: ")
			telefono_fijo = input("Teléfono Fijo: ")
			correo_electronico = input("Correo Electronico: ")
			direccion = input("Dirección: ")

			if not all([tipo_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, correo_electronico, direccion]):
				print("Error: todos los campos son obligatorios.")
				return

			cliente = Cliente(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, telefono_fijo, correo_electronico, direccion)
			self.clientes[numero_identificacion] = cliente
			print("Cliente creado con éxito.")
		except Exception as e: 
			print("Error al registrar al cliente:", e)

	def listar_clientes(self):
		if not self.clientes:
			print("No hay clientes registrados.")
			return
		for c in self.clientes.values(): 
			estado = "Activo" if c.estado else "Inactivo"	
			print(c.numero_identificacion, "-", c.nombres_apellidos, "-", estado)

	def consultar_cliente(self):
		numero_identificacion = input("ID cliente: ") 
		if numero_identificacion in self.clientes: 
			c = self.clientes[numero_identificacion]
			print("Nombre Completo:", c.nombres_apellidos) 
			print("RH Sanguineo:", c.rh_sanguineo)
			print("Teléfono Celular:", c.telefono_celular)
			print("Correo Electronico:", c.correo_electronico)
			print("Estado:", "Activo" if c.estado else "Inactivo")
		else:
			print("Cliente no encontrado.") 

	def actualizar_cliente(self):
		numero_identificacion = input("ID Cliente: ") 
		if numero_identificacion in self.clientes: 
			c = self.clientes[numero_identificacion] 
			c.nombres_apellidos = input("Nuevo Nombre Completo: ") or c.nombres_apellidos
			c.telefono_celular = input("Nuevo Teléfono Celular: ") or c.telefono_celular
			c.correo_electronico = input("Nuevo Correo Electronico: ") or c.correo_electronico
			c.direccion = input("Nueva Dirección: ") or c.direccion
			print("Cliente actualizado.")
		else:
			print("Cliente no encontrado.")

	def eliminar_cliente(self):
		numero = input("ID Cliente a eliminar: ")
		if numero in self.clientes:
			del self.clientes[numero]
			print("Cliente eliminado.")
		else:
			print("Cliente no encontrado.")

	def activar_cliente(self):
		numero = input("ID Cliente: ")
		if numero in self.clientes: 
			self.clientes[numero].activar()
			print("Cliente activado.")
		else:
			print("Cliente no encontrado.")

	def desactivar_cliente(self):
		numero = input("ID cliente: ") 
		if numero in self.clientes: 
			self.clientes[numero].desactivar() 
			print("Cliente desactivado.")
		else:
			print("Cliente no encontrado.")

	def registrar_personal(self):
		numero_identificacion = input("Numero Identificación: ")
		if numero_identificacion in self.personal:
			print("Ya existe.")
			return
		tipo_identificacion = input("Tipo identificación: ")
		nombres_apellidos = input("Nombre Completo: ")
		rh_sanguineo = input("RH Sanguineo: ")
		telefono_celular = input("Teléfono Celular: ")
		rol = input("ROL: ")
		correo_electronico = input("Correo Electronico: ")
		direccion = input("Dirección: ")

		if not all([tipo_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, rol, correo_electronico, direccion]):
			print("Error: todos los campos son obligatorios.")
			return

		p = Personal(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, rol, correo_electronico, direccion)
		self.personal[numero_identificacion] = p
		print("Personal registrado con éxito.")

	def listar_personal(self):
		if not self.personal:
			print("No hay personal registrado.")
			return
		for p in self.personal.values(): 
			estado = "Activo" if p.estado else "Inactivo"
			print(p.numero_identificacion, "-", p.nombres_apellidos, "-", p.rol, "-", estado)

	def consultar_personal(self):
		numero = input("ID personal: ") 
		if numero in self.personal: 
			p = self.personal[numero] 
			print("Nombre:", p.nombres_apellidos) 
			print("Rol:", p.rol) 
			print("Correo:", p.correo_electronico)
		else:
			print("Personal no encontrado.")

	def registrar_procedimiento_administrativo(self):
		codigo = input("Código: ")
		if codigo in self.procesos_administrativos:
			print("El procedimiento ya existe.")
			return
		nombre = input("Nombre del procedimiento: ")
		descripcion = input("Descripción: ")
		if not nombre or not descripcion:
			print("Error: campos obligatorios vacíos.")
			return
		p = ProcedimientoAdministrativo(codigo, nombre, descripcion)
		self.procesos_administrativos[codigo] = p
		print("Procedimiento administrativo registrado.")

	def listar_procedimiento_admistrativo(self):
		if not self.procesos_administrativos:
			print("No hay procedimientos administrativos registrados.")
			return
		for p in self.procesos_administrativos.values():
			print(p.codigo, "-", p.nombre)

	def registrar_procedimiento_medico(self):
		codigo = input("Código: ") 
		if codigo in self.procesos_medicos:
			print("Ya existe.")
			return
		nombre = input("Nombre: ")
		descripcion = input("Descripción: ")
		p = ProcedimientoMedico(codigo, nombre, descripcion)
		self.procesos_medicos[codigo] = p 
		print("Procedimiento médico registrado.") 

	def listar_procedimiento_medico(self):
		if not self.procesos_medicos:
			print("No hay procedimientos médicos registrados.")
			return
		for p in self.procesos_medicos.values():
			print(p.codigo, "-", p.nombre)

	def registrar_historial_medico(self):
		id_cliente = input("ID cliente: ")
		if id_cliente not in self.clientes:
			print("Cliente no existe.")
			return
		codigo = input("Código procedimiento médico: ")
		if codigo not in self.procesos_medicos:
			print("Procedimiento médico no existe.")
			return
		fecha = datetime.now().strftime("%Y-%m-%d")
		registro = HistorialMedico(id_cliente, codigo, fecha)
		self.historial.append(registro)
		print("Historial médico registrado.")

	def historial_fecha(self):
		fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
		encontrado = False
		for h in self.historial:
			if h.fecha == fecha: 
				print("Cliente:", h.id_cliente, "| Procedimiento:", h.procedimiento)
				encontrado = True
		if not encontrado:
			print("No se encontraron registros para esa fecha.")


def main():
	sistema = SistemaClinica()
	while True:
		print("\n BIENVENIDO A LA CLINICA YPSA ")
		print("1. Registrar Cliente")
		print("2. Listar Clientes")
		print("3. Consultar Clientes")
		print("4. Actualizar Clientes")
		print("5. Eliminar Cliente")
		print("6. Activar Cliente")
		print("7 Desactivar Cliente")
		print("\n8. Registrar Personal")
		print("9. Listar Personal")
		print("10. Consultar Personal")
		print("11. Registrar Procedimiento  Administrativo")
		print("12. Listar Procedimiento Administrativo")
		print("\n13. Registrar Procedimiento Medico")
		print("14.Listar procedimiento Medico")
		print("15. Registrar Hsitorial Medico")
		print("16. Consultar Historial Por Fecha")
		print("17. Salir")

		opcion = input("Selecciona una opción: ")

		if opcion == "1": sistema.registrar_cliente()
		elif opcion == "2": sistema.listar_clientes()
		elif opcion == "3": sistema.consultar_cliente()
		elif opcion == "4": sistema.actualizar_cliente()
		elif opcion == "5": sistema.eliminar_cliente()
		elif opcion == "6": sistema.activar_cliente()
		elif opcion == "7": sistema.desactivar_cliente()
		elif opcion == "8": sistema.registrar_personal()
		elif opcion == "9": sistema.listar_personal()
		elif opcion == "10": sistema.consultar_personal()
		elif opcion == "11": sistema.registrar_procedimiento_administrativo()
		elif opcion == "12": sistema.listar_procedimiento_admistrativo()
		elif opcion == "13": sistema.registrar_procedimiento_medico()
		elif opcion == "14": sistema.listar_procedimiento_medico()
		elif opcion == "15": sistema.registrar_historial_medico()
		elif opcion == "16": sistema.historial_fecha()
		elif opcion == "17":
			print("SALIENDO...")
			break
		else:
			print("Opción inválida.")


main()