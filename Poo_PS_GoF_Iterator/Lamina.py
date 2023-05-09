# Clase Lamina:

class Lamina:
    def __init__(self, consecutivo, nombre):
        self.__consecutivo = consecutivo
        self.__nombre = nombre

    def get_consecutivo(self):
        return self.__consecutivo

    def get_nombre(self):
        return self.__nombre

    # EL método __str__ es el método equivalente al ToString de Java y C#
    # Permite escribir el cotenido del objeto
    # Aqui estamos haciendo polimorfismo por sobreescritura
    def __str__(self):
        return f"No. : {self.__consecutivo}, Nombre: {self.__nombre}"
