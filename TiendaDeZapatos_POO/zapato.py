#Clase Zapato:


class Zapato:
    def __init__(self, talla, color, estilo):
        self.__talla = talla
        self.__color = color
        self.__estilo = estilo

    def get_talla(self):
        return self.__talla

    def get_color(self):
        return self.__color

    def get_estilo(self):
        return self.__estilo

    def set_talla(self, talla):
        self.__talla = talla

    def set_color(self, color):
        self.__color = color

    def set_estilo(self, estilo):
        self.__estilo = estilo
