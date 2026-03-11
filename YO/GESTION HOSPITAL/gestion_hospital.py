from datetime import datetime

# ==================================
# CLASE BASE PERSONA
# ==================================

class Persona:

    def __init__(self, tipo_id, numero_id, nombre, rh, celular, correo, direccion):
        self.tipo_id = tipo_id
        self.numero_id = numero_id
        self.nombre = nombre
        self.rh = rh
        self.celular = celular
        self.correo = correo
        self.direccion = direccion
        self.estado = True

    def activar(self):
        self.estado = True

    def desactivar(self):
        self.estado = False


# ==================================
# CLASE CLIENTE
# ==================================

class Cliente(Persona):

    def __init__(self, tipo_id, numero_id, nombre, rh, celular, telefono_fijo, correo, direccion):
        super().__init__(tipo_id, numero_id, nombre, rh, celular, correo, direccion)
        self.telefono_fijo = telefono_fijo


# ==================================
# CLASE PERSONAL
# ==================================

class Personal(Persona):

    def __init__(self, tipo_id, numero_id, nombre, rh, celular, rol, correo, direccion):
        super().__init__(tipo_id, numero_id, nombre, rh, celular, correo, direccion)
        self.rol = rol


# ==================================
# PROCEDIMIENTOS ADMINISTRATIVOS
# ==================================

class ProcedimientoAdministrativo:

    def __init__(self, codigo, nombre, descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion


# ==================================
# PROCEDIMIENTOS MEDICOS
# ==================================

class ProcedimientoMedico:

    def __init__(self, codigo, nombre, descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion


# ==================================
# HISTORIAL MEDICO
# ==================================

class HistorialMedico:

    def __init__(self, id_cliente, procedimiento, fecha):
        self.id_cliente = id_cliente
        self.procedimiento = procedimiento
        self.fecha = fecha


# ==================================
# SISTEMA PRINCIPAL
# ==================================

class SistemaClinica:

    def __init__(self):

        self.clientes = {}
        self.personal = {}
        self.proc_admin = {}
        self.proc_med = {}
        self.historial = []

# ==================================
# VALIDACIONES
# ==================================

    def validar_numero(self, texto):
        return texto.isdigit()

# ==================================
# CRUD CLIENTES
# ==================================

    def registrar_cliente(self):

        try:

            numero = input("Número identificación: ")

            if numero in self.clientes:
                print("Cliente ya existe")
                return

            tipo = input("Tipo ID: ")
            nombre = input("Nombre completo: ")
            rh = input("RH: ")
            celular = input("Celular: ")
            fijo = input("Teléfono fijo: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")

            cliente = Cliente(tipo, numero, nombre, rh, celular, fijo, correo, direccion)

            self.clientes[numero] = cliente

            print("Cliente registrado")

        except:
            print("Error al registrar cliente")

    def listar_clientes(self):

        for c in self.clientes.values():

            estado = "Activo" if c.estado else "Inactivo"

            print(c.numero_id, c.nombre, estado)

    def consultar_cliente(self):

        numero = input("ID cliente: ")

        if numero in self.clientes:

            c = self.clientes[numero]

            print("Nombre:", c.nombre)
            print("RH:", c.rh)
            print("Celular:", c.celular)
            print("Correo:", c.correo)
            print("Estado:", "Activo" if c.estado else "Inactivo")

        else:
            print("Cliente no encontrado")

    def actualizar_cliente(self):

        numero = input("ID cliente: ")

        if numero in self.clientes:

            c = self.clientes[numero]

            c.nombre = input("Nuevo nombre: ")
            c.celular = input("Nuevo celular: ")
            c.correo = input("Nuevo correo: ")
            c.direccion = input("Nueva dirección: ")

            print("Cliente actualizado")

    def eliminar_cliente(self):

        numero = input("ID cliente: ")

        if numero in self.clientes:

            del self.clientes[numero]

            print("Cliente eliminado")

    def activar_cliente(self):

        numero = input("ID cliente: ")

        if numero in self.clientes:

            self.clientes[numero].activar()

            print("Cliente activado")

    def desactivar_cliente(self):

        numero = input("ID cliente: ")

        if numero in self.clientes:

            self.clientes[numero].desactivar()

            print("Cliente desactivado")

# ==================================
# CRUD PERSONAL
# ==================================

    def registrar_personal(self):

        numero = input("Número identificación: ")

        if numero in self.personal:
            print("Ya existe")
            return

        tipo = input("Tipo ID: ")
        nombre = input("Nombre completo: ")
        rh = input("RH: ")
        celular = input("Celular: ")
        rol = input("Rol: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")

        p = Personal(tipo, numero, nombre, rh, celular, rol, correo, direccion)

        self.personal[numero] = p

        print("Personal registrado")

    def listar_personal(self):

        for p in self.personal.values():

            estado = "Activo" if p.estado else "Inactivo"

            print(p.numero_id, p.nombre, p.rol, estado)

    def consultar_personal(self):

        numero = input("ID personal: ")

        if numero in self.personal:

            p = self.personal[numero]

            print("Nombre:", p.nombre)
            print("Rol:", p.rol)
            print("Correo:", p.correo)

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

# ==================================
# PROCEDIMIENTOS ADMINISTRATIVOS
# ==================================

    def registrar_proc_admin(self):

        codigo = input("Código: ")

        if codigo in self.proc_admin:
            print("Ya existe")
            return

        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")

        p = ProcedimientoAdministrativo(codigo, nombre, descripcion)

        self.proc_admin[codigo] = p

        print("Registrado")

    def listar_proc_admin(self):

        for p in self.proc_admin.values():

            print(p.codigo, p.nombre)

    def consultar_proc_admin(self):

        codigo = input("Código: ")

        if codigo in self.proc_admin:

            p = self.proc_admin[codigo]

            print(p.nombre)
            print(p.descripcion)

    def actualizar_proc_admin(self):

        codigo = input("Código: ")

        if codigo in self.proc_admin:

            p = self.proc_admin[codigo]

            p.nombre = input("Nuevo nombre: ")
            p.descripcion = input("Nueva descripción")

# ==================================
# PROCEDIMIENTOS MEDICOS
# ==================================

    def registrar_proc_medico(self):

        codigo = input("Código: ")

        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")

        p = ProcedimientoMedico(codigo, nombre, descripcion)

        self.proc_med[codigo] = p

        print("Registrado")

    def listar_proc_medico(self):

        for p in self.proc_med.values():

            print(p.codigo, p.nombre)

    def consultar_proc_medico(self):

        codigo = input("Código: ")

        if codigo in self.proc_med:

            p = self.proc_med[codigo]

            print(p.nombre)
            print(p.descripcion)

    def actualizar_proc_medico(self):

        codigo = input("Código: ")

        if codigo in self.proc_med:

            p = self.proc_med[codigo]

            p.nombre = input("Nuevo nombre: ")
            p.descripcion = input("Nueva descripción")

# ==================================
# HISTORIAL MEDICO
# ==================================

    def registrar_historial(self):

        id_cliente = input("ID cliente: ")

        if id_cliente not in self.clientes:
            print("Cliente no existe")
            return

        codigo = input("Código procedimiento médico: ")

        if codigo not in self.proc_med:
            print("Procedimiento no existe")
            return

        fecha = datetime.now().strftime("%Y-%m-%d")

        registro = HistorialMedico(id_cliente, codigo, fecha)

        self.historial.append(registro)

        print("Procedimiento registrado")

    def consultar_historial_fecha(self):

        fecha = input("Ingrese fecha (YYYY-MM-DD): ")

        for h in self.historial:

            if h.fecha == fecha:

                print("Cliente:", h.id_cliente, "Procedimiento:", h.procedimiento)


# ==================================
# MENU PRINCIPAL
# ==================================

def main():

    sistema = SistemaClinica()

    while True:

        print("\n==== CLINICA YPSA ====")

        print("1 Registrar cliente")
        print("2 Listar clientes")
        print("3 Consultar cliente")
        print("4 Actualizar cliente")
        print("5 Eliminar cliente")
        print("6 Activar cliente")
        print("7 Desactivar cliente")

        print("\n8 Registrar personal")
        print("9 Listar personal")
        print("10 Consultar personal")

        print("\n11 Registrar procedimiento administrativo")
        print("12 Listar procedimientos administrativos")

        print("\n13 Registrar procedimiento medico")
        print("14 Listar procedimientos medicos")

        print("\n15 Registrar historial medico")
        print("16 Consultar historial por fecha")

        print("\n0 Salir")

        op = input("Seleccione opción: ")

        if op == "1":
            sistema.registrar_cliente()

        elif op == "2":
            sistema.listar_clientes()

        elif op == "3":
            sistema.consultar_cliente()

        elif op == "4":
            sistema.actualizar_cliente()

        elif op == "5":
            sistema.eliminar_cliente()

        elif op == "6":
            sistema.activar_cliente()

        elif op == "7":
            sistema.desactivar_cliente()

        elif op == "8":
            sistema.registrar_personal()

        elif op == "9":
            sistema.listar_personal()

        elif op == "10":
            sistema.consultar_personal()

        elif op == "11":
            sistema.registrar_proc_admin()

        elif op == "12":
            sistema.listar_proc_admin()

        elif op == "13":
            sistema.registrar_proc_medico()

        elif op == "14":
            sistema.listar_proc_medico()

        elif op == "15":
            sistema.registrar_historial()

        elif op == "16":
            sistema.consultar_historial_fecha()

        elif op == "0":
            print("Sistema finalizado")
            break


main()