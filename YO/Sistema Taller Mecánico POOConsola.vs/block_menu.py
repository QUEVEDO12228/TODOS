from sistema import Sistema
def pausa():
    input("\nPresione ENTER para continuar...")
def main():
    sistema = Sistema()
    print("===== SISTEMA TALLER MECÁNICO =====")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    if not sistema.usuario.login(username, password):
        print("Credenciales incorrectas.")
        pausa()
        return
    print("\nLogin exitoso.")
    pausa()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de Vehículos")
        print("2. Gestión de Órdenes")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            while True:
                print("\n--- GESTIÓN VEHÍCULOS ---")
                print("1. Crear Vehículo")
                print("2. Listar Vehículos")
                print("3. Actualizar Vehículo")
                print("4. Eliminar Vehículo")
                print("5. Volver")
                op_v = input("Seleccione una opción: ")
                if op_v == "1":
                    placa = input("Placa: ")
                    marca = input("Marca: ")
                    modelo = input("Modelo: ")
                    anio = input("Año: ")
                    propietario = input("Propietario: ")
                    telefono = input("Teléfono: ")
                    sistema.crear_vehiculo(placa, marca, modelo, anio, propietario, telefono)
                    pausa()
                elif op_v == "2":
                    sistema.listar_vehiculos()
                    pausa()
                elif op_v == "3":
                    placa = input("Ingrese placa del vehículo a actualizar: ")
                    sistema.actualizar_vehiculo(placa)
                    pausa()
                elif op_v == "4":
                    placa = input("Ingrese placa del vehículo a eliminar: ")
                    sistema.eliminar_vehiculo(placa)
                    pausa()
                elif op_v == "5":
                    break
                else:
                    print("Opción inválida.")
                    pausa()
        elif opcion == "2":
            while True:
                print("\n--- GESTIÓN ÓRDENES ---")
                print("1. Crear Orden")
                print("2. Listar Órdenes")
                print("3. Actualizar Orden")
                print("4. Eliminar Orden")
                print("5. Volver")
                op_o = input("Seleccione una opción: ")
                if op_o == "1":
                    placa = input("Placa del vehículo: ")
                    descripcion = input("Descripción: ")
                    estado = input("Estado: ")
                    costo = float(input("Costo estimado: "))
                    sistema.crear_orden(placa, descripcion, estado, costo)
                    pausa()
                elif op_o == "2":
                    sistema.listar_ordenes()
                    pausa()
                elif op_o == "3":
                    descripcion = input("Ingrese descripción de la orden a actualizar: ")
                    sistema.actualizar_orden(descripcion)
                    pausa()
                elif op_o == "4":
                    descripcion = input("Ingrese descripción de la orden a eliminar: ")
                    sistema.eliminar_orden(descripcion)
                    pausa()
                elif op_o == "5":
                    break
                else:
                    print("Opción inválida.")
                    pausa()
        elif opcion == "3":
            print("Sesión cerrada.")
            pausa()
            break
        else:
            print("Opción inválida.")
            pausa()
if __name__ == "__main__":
    main()
    