# Clase Album
from abc import ABC
from IColeccionAbstracta import IColeccionAbstracta


class Album(IColeccionAbstracta, ABC):
    def __init__(self, lasLaminas, nombre):
        self.__lasLaminas = lasLaminas
        self.__nombre = nombre

    def set_lamina(self, unaLamina):
        self.__lasLaminas.append(unaLamina)

    def get_lamina(self, posicion):
        return self.__lasLaminas[posicion]

