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

    def __init__(self, tipo_identificacion, numero_identificacion, nombre, rh, celular, telefono_fijo, correo, direccion):
        super().__init__(tipo_identificacion, numero_identificacion, nombre, rh, celular, correo, direccion)
        self.telefono_fijo = telefono_fijo

class Personal:
    def __init__(self, tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, rol, correo_electronico, direccion):
        super().__init__(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, correo_electronico, direccion)
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
        self.proc_med = {}
        self.historial = []

    def validar_numero(self, texto):
        return texto.isdigit() 
    def registrar_cliente(self):
        try:
            numero_identificacion = input("Numero de Identificación: ")
            if numero_identificacion in self.clientes: 
                print("Cliente ya existe")
                return 
            tipo_identificacion = input("Tipo ID: ")
            nombres_apellidos = input("Nombre Completo: ")
            rh_sanguineo = input("RH Sanguineo: ")
            telefono_celular = input("Teléfono Celular: ")
            telefono_fijo = input("Teléfono Fijo: ")
            correo_electronico = input("Correo Electronico: ")
            direccion = input("Dirección: ")
            cliente = Cliente(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, telefono_fijo, 
                            correo_electronico, direccion)
            self.clientes[numero_identificacion] = cliente
            print("Cliente creado con exito")
        except: 
            print("Error al registrar al cliente")

    def listar_clientes(self):
        for c in self.clientes.values(): 
            estado = "Activo" if c.estado else "Inactivo"	
            print(c.numero_identificacion, c.nombres_apellidos, estado) 
	
    def consultar_cliente(self):
        numero_identificacion = input("ID cliente: ") 
        if numero_identificacion in self.clientes: 
            c = self.clientes[numero_identificacion]
            print("Nombre Completo:", c.nombres_apellidos) 
            print("RH Sanguineo: ", c.rh_sanguineo)
            print("Telefono Celular:", c.telefono_celular)
            print("Correo Electronico:", c.correo_electronico)
            print("Estado: ","Activo" if c.estado else "Inactivo")
        else:
            print("Cliente no Encontrado") 

    def actualizar_cliente(self)
        numero_identificacion = input("ID Cliente: ") 
        if numero_identificacion in self.clientes: 
            c = self.clientes[numero_identificacion] 
            c.nombres_apellidos = input("Nuevo Nombre Completo: ")
            c.telefono_celular = input("Nuevo Teléfono Celular: ")
            c.correo_electronico = input("Nuevo Correo Electronico")
            c.direccion = input("Nueva Dirección: ")
            print("Cliente Actualizado")
    
    def eliminar_cliente(self):
        numero = input("ID Cliente a eliminar: ")
        if numero in self.clientes:
            del self.clientes[numero]
            print("Cliente Eliminado")
    
    def activar_cliente(self):
        numero = input("ID Cliente: ")
        if numero in self.clientes: 
            self.clientes[numero].activar()
            print("Cliente Activado")

    def desactivar_cliente(self):
        numero = input("ID cliente: ") 
        if numero in self.clientes: 
            self.clientes[numero].desactivar() 
            print("Cliente desactivado")

    def registrar_personal(self):
        numero_identificacion = input("Numero Identificación: ")
        if numero_identificacion in self.personal:
            print("Ya existe")
            return
        tipo_identificacion = input("Tipo identificacion: ")
        nombres_apellidos = input("Nombre Completo: ")
        rh_sanguineo = input("RH Sanguineo: ")
        telefono_celular = input("Teléfono Celular: ")
        rol = input("ROL: ")
        correo_electronico = input("Correo Electronico: ")
        direccion = input("Dirección: ")
        p = Personal(tipo_identificacion, numero_identificacion, nombres_apellidos, rh_sanguineo, telefono_celular, rol, correo_electronico, direccion)
        self.personal[numero_identificacion] p 
        print("Personal registrado")

    def listar_personal(self):
        for p in self.personal.values(): 
            estado "Activo" if p.estado else "Inactivo"
            print(p.numero_identificacion, p.nombres_apellidos, p.rol, estado)

	def consultar_personal(Self):
		numero = input("ID personal: ") 
		if numero in self.personal: p = self.personal[numero] 
			print("Nombre:", p.nombre) print("Rol:", p.rol) print("Correo:", p.correo) 
	def actualizar_personal(self): 
		numero = input("ID personal: ") 
		if numero in self.personal: 
		p = self.personal[numero] 
		p.nombre = input("Nuevo nombre: ") 
		p.rol = input("Nuevo rol: ") 
		p.celular = input("Nuevo celular: ") 
		print("Actualizado") 
	def eliminar_personal(self): 
		numero = input("ID personal: ") 
		if numero in self.personal: 
		del self.personal[numero] 
			print("Eliminado") 
	def activar_personal(self): 
		numero = input("ID personal: ") 
		if numero in self.personal: 
		self.personal[numero].activar() 
	def desactivar_personal(self): 
		numero = input("ID personal: ") 
		if numero in self.personal: 
		self.personal[numero].desactivar() 
	def registrar_procesos_administrativos(self):
		codigo = input("Codigo: ")
		if codigo in self.procesos_administrativos:
			print("Ya existe")
		 
	def listar_procesos_administrativos(self):
		for o in self.procesos_administrativos.values():
		print(p.codigo, p.nombre) 
	def consultar_procesos_administrativos(self):
		codigo = input("codigo: ")
		if codigo in self.procesos_administrativos: 
		p = self.procesos_aministrativos[codigo]
 		print(p.nombre) 
		print(p.descripcion)
	def actualizar_procesos_administrativos(Self):
		codigo = input("codigo: ") 
		if codigo in self_procesos_administrativos: 
		p = self.procesos_administrativos[codigo] 
		p.nombre = input("Nuevo Nombre: ")
		p.descripcion = input("Nueva Descripción: ")
	
	