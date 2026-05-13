# =====================================================
# ARCHIVO PRINCIPAL - main.py
# SISTEMA DE RESERVAS SOFTWARE FJ
# =====================================================

# =====================================================
# IMPORTACIÓN DE MÓDULOS
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


# =====================================================
# LISTAS PRINCIPALES DEL SISTEMA
# =====================================================

clientes = []
servicios = []
reservas = []


# =====================================================
# FUNCIÓN REGISTRAR CLIENTE
# =====================================================

def registrar_cliente():

    try:

        print("\n========== REGISTRO DE CLIENTE ==========")

        nombre = input("Nombre: ").strip()
        documento = input("Documento: ").strip()
        correo = input("Correo: ").strip()

        # =============================================
        # VALIDACIONES
        # =============================================

        if nombre == "":
            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        if documento == "":
            raise ClienteError(
                "El documento no puede estar vacío"
            )

        if "@" not in correo:
            raise ClienteError(
                "Correo inválido"
            )

        # =============================================
        # CREAR CLIENTE
        # =============================================

        cliente = Cliente(
            nombre,
            documento,
            correo
        )

        clientes.append(cliente)

        registrar_log(
            "Cliente registrado correctamente"
        )

        print("\nCliente registrado exitosamente")

    except ClienteError as error:

        registrar_log(error)

        print("\nError:", error)


# =====================================================
# FUNCIÓN REGISTRAR SERVICIO
# =====================================================

def registrar_servicio():

    try:

        print("\n========== REGISTRO DE SERVICIO ==========")

        print("1. Reserva de sala")
        print("2. Alquiler de equipo")
        print("3. Asesoría especializada")

        tipo = input(
            "\nSeleccione tipo de servicio: "
        )

        nombre = input(
            "Nombre del servicio: "
        ).strip()

        # =============================================
        # VALIDAR NOMBRE
        # =============================================

        if nombre == "":
            raise ServicioError(
                "El nombre del servicio es obligatorio"
            )

        # =============================================
        # VALIDAR TARIFA
        # =============================================

        tarifa = float(
            input("Tarifa base: ")
        )

        if tarifa <= 0:

            raise ServicioError(
                "La tarifa debe ser mayor a cero"
            )

        # =============================================
        # RESERVA DE SALA
        # =============================================

        if tipo == "1":

            capacidad = int(
                input("Capacidad de la sala: ")
            )

            if capacidad <= 0:

                raise ServicioError(
                    "La capacidad debe ser mayor a cero"
                )

            servicio = ReservaSala(
                nombre,
                tarifa,
                capacidad
            )

        # =============================================
        # ALQUILER DE EQUIPO
        # =============================================

        elif tipo == "2":

            equipo = input(
                "Tipo de equipo: "
            ).strip()

            if equipo == "":

                raise ServicioError(
                    "Debe indicar el tipo de equipo"
                )

            servicio = AlquilerEquipo(
                nombre,
                tarifa,
                equipo
            )

        # =============================================
        # ASESORÍA ESPECIALIZADA
        # =============================================

        elif tipo == "3":

            especialista = input(
                "Nombre del especialista: "
            ).strip()

            if especialista == "":

                raise ServicioError(
                    "Debe indicar el especialista"
                )

            servicio = AsesoriaEspecializada(
                nombre,
                tarifa,
                especialista
            )

        # =============================================
        # OPCIÓN INVÁLIDA
        # =============================================

        else:

            raise ServicioError(
                "Tipo de servicio inválido"
            )

        # =============================================
        # GUARDAR SERVICIO
        # =============================================

        servicios.append(servicio)

        registrar_log(
            "Servicio registrado correctamente"
        )

        print("\nServicio registrado exitosamente")

    except ValueError:

        print(
            "\nError: Debe ingresar valores numéricos válidos"
        )

    except ServicioError as error:

        registrar_log(error)

        print("\nError:", error)


# =====================================================
# FUNCIÓN CREAR RESERVA
# =====================================================

def crear_reserva():

    try:

        # =============================================
        # VALIDAR CLIENTES
        # =============================================

        if len(clientes) == 0:

            raise ReservaError(
                "No hay clientes registrados"
            )

        # =============================================
        # VALIDAR SERVICIOS
        # =============================================

        if len(servicios) == 0:

            raise ReservaError(
                "No hay servicios registrados"
            )

        # =============================================
        # MOSTRAR CLIENTES
        # =============================================

        print("\n========== CLIENTES ==========")

        for i, cliente in enumerate(clientes):

            print(
                str(i) + ". " + cliente.nombre
            )

        indice_cliente = int(
            input("\nSeleccione cliente: ")
        )

        # =============================================
        # VALIDAR CLIENTE
        # =============================================

        if (
            indice_cliente < 0 or
            indice_cliente >= len(clientes)
        ):

            raise ReservaError(
                "Cliente inválido"
            )

        # =============================================
        # MOSTRAR SERVICIOS
        # =============================================

        print("\n========== SERVICIOS ==========")

        for i, servicio in enumerate(servicios):

            print(
                str(i) + ". " + servicio.nombre
            )

        indice_servicio = int(
            input("\nSeleccione servicio: ")
        )

        # =============================================
        # VALIDAR SERVICIO
        # =============================================

        if (
            indice_servicio < 0 or
            indice_servicio >= len(servicios)
        ):

            raise ReservaError(
                "Servicio inválido"
            )

        # =============================================
        # HORAS DE RESERVA
        # =============================================

        horas = int(
            input("Horas de reserva: ")
        )

        if horas <= 0:

            raise ReservaError(
                "Las horas deben ser mayores a cero"
            )

        # =============================================
        # CREAR RESERVA
        # =============================================

        reserva = Reserva(
            clientes[indice_cliente],
            servicios[indice_servicio],
            horas
        )

        # =============================================
        # PROCESAR RESERVA
        # =============================================

        costo = reserva.procesar()

        reservas.append(reserva)

        print("\nReserva creada correctamente")

        print(
            "Costo total: $" + str(costo)
        )

        registrar_log(
            "Reserva creada correctamente"
        )

    except ValueError:

        print(
            "\nError: Debe ingresar números válidos"
        )

    except ReservaError as error:

        registrar_log(error)

        print("\nError:", error)


# =====================================================
# FUNCIÓN MOSTRAR RESERVAS
# =====================================================

def mostrar_reservas():

    print("\n========== RESERVAS ==========")

    if len(reservas) == 0:

        print("\nNo hay reservas registradas")

    else:

        for reserva in reservas:

            print(
                "\nCliente:",
                reserva.cliente.nombre
            )

            print(
                "Servicio:",
                reserva.servicio.nombre
            )

            print(
                "Estado:",
                reserva.estado
            )

            if hasattr(reserva, "horas"):

                print(
                    "Horas:",
                    reserva.horas
                )

            print("-----------------------------")


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

while True:

    print("\n====================================")
    print("      SISTEMA DE RESERVAS FJ")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Salir")
    print("6. Ver resumen del sistema")

    opcion = input(
        "\nSeleccione una opción: "
    )

    # =============================================
    # OPCIÓN 1
    # =============================================

    if opcion == "1":

        registrar_cliente()

    # =============================================
    # OPCIÓN 2
    # =============================================

    elif opcion == "2":

        registrar_servicio()

    # =============================================
    # OPCIÓN 3
    # =============================================

    elif opcion == "3":

        crear_reserva()

    # =============================================
    # OPCIÓN 4
    # =============================================

    elif opcion == "4":

        mostrar_reservas()

    # =============================================
    # OPCIÓN 5
    # =============================================

    elif opcion == "5":

        print("\nSaliendo del sistema...")
        print("Hasta luego")

        break

    # =============================================
    # OPCIÓN INVÁLIDA
    # =============================================

    elif opcion == "6":
        print("\n========== RESUMEN DEL SISTEMA ==========")
        print("Clientes registrados:", len(clientes))
        print("Servicios registrados:", len(servicios))
        print("Reservas registradas:", len(reservas))

    else:

        print("\nOpción inválida")
