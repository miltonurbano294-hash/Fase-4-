from abc import ABC, abstractmethod
from Excepciones import ClienteError


# =====================================================
# CLASE ABSTRACTA BASE
# =====================================================

class Entidad(ABC):

    # Método obligatorio para las clases hijas
    @abstractmethod
    def mostrar_info(self):
        pass


# =====================================================
# CLASE CLIENTE
# =====================================================

class Cliente(Entidad):

    # =============================================
    # CONSTRUCTOR
    # =============================================

    def __init__(self, nombre, documento, correo):

        # =========================================
        # VALIDAR NOMBRE
        # =========================================

        if nombre.strip() == "":

            raise ClienteError(
                "El nombre está vacío"
            )

        # =========================================
        # VALIDAR DOCUMENTO
        # =========================================

        if len(documento) < 5:

            raise ClienteError(
                "Documento inválido"
            )

        # =========================================
        # VALIDAR CORREO
        # =========================================

        if "@" not in correo:

            raise ClienteError(
                "Correo inválido"
            )

        # =========================================
        # ATRIBUTOS PRIVADOS
        # =========================================

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    # =============================================
    # GETTERS
    # =============================================

    @property
    def nombre(self):

        return self.__nombre

    @property
    def documento(self):

        return self.__documento

    @property
    def correo(self):

        return self.__correo

    # =============================================
    # MOSTRAR INFORMACIÓN
    # =============================================

    def mostrar_info(self):

        return (
            "Cliente: {0} | Documento: {1}"
        ).format(
            self.__nombre,
            self.__documento
        )
