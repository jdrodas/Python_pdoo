# Interface IColeccionAbstracta

from abc import ABC, abstractmethod


class IColeccionAbstracta(ABC):
    @abstractmethod
    def crear_iterador(self):
        pass
