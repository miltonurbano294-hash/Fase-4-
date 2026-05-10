# =====================================================
# ARCHIVO PRINCIPAL - main.py
# SISTEMA DE RESERVAS SOFTWARE FJ
# =====================================================

from Clientes import Cliente

from Servicios import ReservaSala
from Servicios import AlquilerEquipo
from Servicios import AsesoriaEspecializada

from Reservas import Reserva

from Excepciones import ClienteError
from Excepciones import ServicioError
from Excepciones import ReservaError

from Utilidades import registrar_log


# ============================================
# LISTAS DEL SISTEMA
# ============================================

clientes = []
servicios = []
reservas = []


# ============================================
# MENÚ PRINCIPAL
# ============================================

while True:

    print("\n====================================")
    print("      SISTEMA DE RESERVAS FJ")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")


    # ========================================
    # REGISTRAR CLIENTE
    # ========================================

    if opcion == "1":

        try:

            print("\n--- REGISTRO DE CLIENTE ---")

            nombre = input("Nombre: ")
            documento = input("Documento: ")
            correo = input("Correo: ")

            cliente = Cliente(
                nombre,
                documento,
                correo
            )

            clientes.append(cliente)

            registrar_log("Cliente registrado correctamente")

            print("\nCliente registrado exitosamente")

        except ClienteError as error:

            registrar_log(error)

            print("\nError:", error)


    # ========================================
    # REGISTRAR SERVICIO
    # ========================================

    elif opcion == "2":

        try:

            print("\n--- REGISTRO DE SERVICIO ---")

            print("1. Reserva de sala")
            print("2. Alquiler de equipo")
            print("3. Asesoría especializada")

            tipo = input("\nSeleccione tipo de servicio: ")

            nombre = input("Nombre del servicio: ")

            tarifa = float(
                input("Tarifa base: ")
            )


            # ================================
            # SALA
            # ================================

            if tipo == "1":

                capacidad = int(
                    input("Capacidad de la sala: ")
                )

                servicio = ReservaSala(
                    nombre,
                    tarifa,
                    capacidad
                )


            # ================================
            # EQUIPO
            # ================================

            elif tipo == "2":

                equipo = input(
                    "Tipo de equipo: "
                )

                servicio = AlquilerEquipo(
                    nombre,
                    tarifa,
                    equipo
                )


            # ================================
            # ASESORÍA
            # ================================

            elif tipo == "3":

                especialista = input(
                    "Nombre del especialista: "
                )

                servicio = AsesoriaEspecializada(
                    nombre,
                    tarifa,
                    especialista
                )

            else:
                raise ServicioError(
                    "Tipo de servicio inválido"
                )


            servicios.append(servicio)

            registrar_log(
                "Servicio agregado correctamente"
            )

            print("\nServicio registrado correctamente")


        except Exception as error:

            registrar_log(error)

            print("\nError:", error)


    # ========================================
    # CREAR RESERVA
    # ========================================

    elif opcion == "3":

        try:

            if len(clientes) == 0:
                raise ReservaError(
                    "No hay clientes registrados"
                )

            if len(servicios) == 0:
                raise ReservaError(
                    "No hay servicios registrados"
                )

            print("\n===== CLIENTES =====")

            i = 0

            while i < len(clientes):

                print(
                    str(i) + ". " +
                    clientes[i].nombre
                )

                i += 1


            indice_cliente = int(
                input("\nSeleccione cliente: ")
            )


            print("\n===== SERVICIOS =====")

            i = 0

            while i < len(servicios):

                print(
                    str(i) + ". " +
                    servicios[i].nombre
                )

                i += 1


            indice_servicio = int(
                input("\nSeleccione servicio: ")
            )

            horas = int(
                input("Horas de reserva: ")
            )


            reserva = Reserva(
                clientes[indice_cliente],
                servicios[indice_servicio],
                horas
            )


            costo = reserva.procesar()

            reservas.append(reserva)


            print("\nReserva realizada correctamente")

            print(
                "Costo total: $" +
                str(costo)
            )

            registrar_log(
                "Reserva creada correctamente"
            )


        except Exception as error:

            registrar_log(error)

            print("\nError:", error)


    # ========================================
    # VER RESERVAS
    # ========================================

    elif opcion == "4":

        print("\n========== RESERVAS ==========")

        if len(reservas) == 0:

            print("\nNo hay reservas registradas")

        else:

            for reserva in reservas:

                print("\nCliente:",
                      reserva.cliente.nombre)

                print("Servicio:",
                      reserva.servicio.nombre)

                print("Estado:",
                      reserva.estado)

                print("-----------------------------")


    # ========================================
    # SALIR
    # ========================================

    elif opcion == "5":

        print("\nSaliendo del sistema...")
        print("Hasta luego")

        break


    # ========================================
    # OPCIÓN INVÁLIDA
    # ========================================

    else:

        print("\nOpción inválida")