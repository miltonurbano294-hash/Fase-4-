# Archivo: servicios.py

# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Importamos la excepción personalizada
from Excepciones import ServicioError


# ---------------------------------------------------
# Clase abstracta Servicio
# Sirve como base para otros servicios
# ---------------------------------------------------
class Servicio(ABC):

    # Constructor principal
    def __init__(self, nombre, tarifa_base):

        # Validamos que la tarifa sea mayor a 0
        if tarifa_base <= 0:
            raise ServicioError("La tarifa debe ser mayor que cero")

        # Atributos del servicio
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    # Método abstracto para calcular costos
    # Cada clase hija debe implementarlo
    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    # Método abstracto para mostrar descripción
    @abstractmethod
    def descripcion(self):
        pass


# ---------------------------------------------------
# Clase ReservaSala
# Hereda de Servicio
# ---------------------------------------------------
class ReservaSala(Servicio):

    # Constructor
    def __init__(self, nombre, tarifa_base, capacidad):

        # Llamamos al constructor de la clase padre
        Servicio.__init__(self, nombre, tarifa_base)

        # Guardamos capacidad de la sala
        self.capacidad = capacidad

    # Método para calcular costo
    def calcular_costo(self, horas, descuento=0):

        # Validamos horas
        if horas <= 0:
            raise ServicioError("Horas inválidas")

        # Calculamos total
        total = self.tarifa_base * horas

        # Aplicamos descuento
        total = total - (total * descuento)

        return total

    # Método adicional con impuesto opcional
    def calcular_costo_impuestos(self, horas, impuesto=0.19):

        # Calculamos subtotal
        subtotal = self.calcular_costo(horas)

        # Retornamos subtotal + impuesto
        return subtotal + (subtotal * impuesto)

    # Método descripción
    def descripcion(self):

        return "Sala para {0} personas".format(self.capacidad)


# ---------------------------------------------------
# Clase AlquilerEquipo
# Hereda de Servicio
# ---------------------------------------------------
class AlquilerEquipo(Servicio):

    # Constructor
    def __init__(self, nombre, tarifa_base, tipo_equipo):

        # Llamamos al constructor padre
        Servicio.__init__(self, nombre, tarifa_base)

        # Tipo de equipo
        self.tipo_equipo = tipo_equipo

    # Método para calcular costo
    def calcular_costo(self, horas, descuento=0):

        # Validación de horas
        if horas <= 0:
            raise ServicioError("Horas inválidas")

        # Cálculo total
        total = self.tarifa_base * horas

        # Aplicamos descuento
        return total - (total * descuento)

    # Método descripción
    def descripcion(self):

        return "Equipo tipo {0}".format(self.tipo_equipo)


# ---------------------------------------------------
# Clase AsesoriaEspecializada
# Hereda de Servicio
# ---------------------------------------------------
class AsesoriaEspecializada(Servicio):

    # Constructor
    def __init__(self, nombre, tarifa_base, especialista):

        # Constructor de la clase padre
        Servicio.__init__(self, nombre, tarifa_base)

        # Nombre del especialista
        self.especialista = especialista

    # Método calcular costo
    def calcular_costo(self, horas, descuento=0):

        # Validamos horas
        if horas <= 0:
            raise ServicioError("Horas inválidas")

        # Calculamos valor base
        total = self.tarifa_base * horas

        # Agregamos recargo del 15%
        total += total * 0.15

        # Aplicamos descuento
        total -= total * descuento

        return total

    # Método descripción
    def descripcion(self):

        return "Asesoría realizada por {0}".format(
            self.especialista
        )
