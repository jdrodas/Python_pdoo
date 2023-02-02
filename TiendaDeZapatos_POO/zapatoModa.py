# Clase ZapatoModa que hereda de Zapato
from zapato import Zapato


class ZapatoModa(Zapato):

    def __init__(self, talla, color, estilo, cantidad):
        super().__init__(talla, color, estilo)
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"{super().__str__()}, Cantidad: {self.__cantidad}"
