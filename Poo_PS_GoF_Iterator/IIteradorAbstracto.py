# Interface IIteradorAbstracto

from abc import ABC, abstractmethod


class IIteradorAbstracto(ABC):
    @abstractmethod
    def primera(self):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def esta_terminado(self):
        pass

    @abstractmethod
    def lamina_actual(self):
        pass
