class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password
class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, propietario, telefono):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.propietario = propietario
        self.telefono = telefono
class OrdenReparacion:
    def __init__(self, placa, descripcion, estado, costo):
        self.placa = placa
        self.descripcion = descripcion
        self.estado = estado
        self.costo = costo
class Sistema:
    def __init__(self):
        self.usuario = Usuario("admin", "1234")
        self.vehiculos = []
        self.ordenes = []
    def crear_vehiculo(self, placa, marca, modelo, anio, propietario, telefono):
        for v in self.vehiculos:
            if v.placa == placa:
                print("Ya existe un vehículo con esa placa.")
                return
        nuevo = Vehiculo(placa, marca, modelo, anio, propietario, telefono)
        self.vehiculos.append(nuevo)
        print("Vehículo registrado correctamente.")
    def listar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
            return
        for v in self.vehiculos:
            print(f"Placa: {v.placa} | Marca: {v.marca} | Modelo: {v.modelo} | Año: {v.anio} | Propietario: {v.propietario}")
    def actualizar_vehiculo(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                v.marca = input("Nueva marca: ")
                v.modelo = input("Nuevo modelo: ")
                v.anio = input("Nuevo año: ")
                v.propietario = input("Nuevo propietario: ")
                v.telefono = input("Nuevo teléfono: ")
                print("Vehículo actualizado correctamente.")
                return
        print("Vehículo no encontrado.")
    def eliminar_vehiculo(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                self.vehiculos.remove(v)
                print("Vehículo eliminado correctamente.")
                return
        print("Vehículo no encontrado.")
    def crear_orden(self, placa, descripcion, estado, costo):
        existe = False
        for v in self.vehiculos:
            if v.placa == placa:
                existe = True
                break
        if not existe:
            print("No existe un vehículo con esa placa.")
            return
        nueva = OrdenReparacion(placa, descripcion, estado, costo)
        self.ordenes.append(nueva)
        print("Orden creada correctamente.")
    def listar_ordenes(self):
        if not self.ordenes:
            print("No hay órdenes registradas.")
            return
        for o in self.ordenes:
            print(f"Vehículo: {o.placa} | Descripción: {o.descripcion} | Estado: {o.estado} | Costo: {o.costo}")
    def actualizar_orden(self, descripcion):
        for o in self.ordenes:
            if o.descripcion == descripcion:
                o.estado = input("Nuevo estado: ")
                o.costo = float(input("Nuevo costo: "))
                print("Orden actualizada correctamente.")
                return
        print("Orden no encontrada.")
    def eliminar_orden(self, descripcion):
        for o in self.ordenes:
            if o.descripcion == descripcion:
                self.ordenes.remove(o)
                print("Orden eliminada correctamente.")
                return
        print("Orden no encontrada.")