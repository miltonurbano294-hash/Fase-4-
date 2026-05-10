# Archivo: servicios.py
from abc import ABC, abstractmethod
from Excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        if tarifa_base <= 0:
            raise ServicioError("La tarifa debe ser mayor que cero")

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad):

        Servicio.__init__(self, nombre, tarifa_base)

        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        total = self.tarifa_base * horas

        total = total - (total * descuento)

        return total

    # Método con parámetros opcionales
    def calcular_costo_impuestos(self, horas, impuesto=0.19):

        subtotal = self.calcular_costo(horas)

        return subtotal + (subtotal * impuesto)

    def descripcion(self):

        return "Sala para {0} personas".format(self.capacidad)


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, tipo_equipo):

        Servicio.__init__(self, nombre, tarifa_base)

        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        total = self.tarifa_base * horas

        return total - (total * descuento)

    def descripcion(self):

        return "Equipo tipo {0}".format(self.tipo_equipo)


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa_base, especialista):

        Servicio.__init__(self, nombre, tarifa_base)

        self.especialista = especialista

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        total = self.tarifa_base * horas

        # Recargo por asesoría especializada
        total += total * 0.15

        total -= total * descuento

        return total

    def descripcion(self):

        return "Asesoría realizada por {0}".format(
            self.especialista
        )