from abc import ABC, abstractmethod
from Excepciones import ClienteError


class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):

    def __init__(self, nombre, documento, correo):

        # Validaciones básicas
        if nombre.strip() == "":
            raise ClienteError("El nombre está vacío")

        if len(documento) < 5:
            raise ClienteError("Documento inválido")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        # Encapsulación
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):

        return "Cliente: {0} | Documento: {1}".format(
            self.__nombre,
            self.__documento
        )