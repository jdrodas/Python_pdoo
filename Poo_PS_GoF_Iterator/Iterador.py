# Clase Iterador
from abc import ABC
from IIteradorAbstracto import IIteradorAbstracto


class Iterador(IIteradorAbstracto, ABC):
    def __init__(self, la_coleccion):
        self.__una_coleccion = la_coleccion
        self.__actual = 0
        self.__incremento = 1

    def get_incremento(self):
        return self.__incremento

    def set_incremento(self, incremento):
        self.__incremento = incremento

    def primera(self):
        __actual = 0
        return self.__una_coleccion[__actual]

    def siguiente(self):
        self.__actual = self.__actual + self.__incremento
        if not self.esta_terminado():
            return self.__una_coleccion[self.__actual]
        else:
            pass

    def esta_terminado(self):
        if self.__actual >= self.__una_coleccion.count():
            return True
        else:
            return False

    def lamina_actual(self):
        return self.__una_coleccion[self.__actual]