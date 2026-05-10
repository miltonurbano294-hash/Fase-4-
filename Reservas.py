from Clientes import Cliente
from Servicios import Servicio
from Excepciones import ReservaError
from Utilidades import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, horas):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

        registrar_log(
            "Reserva confirmada para {0}".format(
                self.cliente.nombre
            )
        )

    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            "Reserva cancelada para {0}".format(
                self.cliente.nombre
            )
        )

    def procesar(self):

        try:
            costo = self.servicio.calcular_costo(self.horas)

        except Exception as error:

            raise ReservaError(
                "No fue posible procesar la reserva"
            ) from error

        else:

            self.confirmar()

            return costo

        finally:
            registrar_log("Proceso de reserva ejecutado")