# Clase Zapato:

class Zapato:
    def __init__(self, talla, color, estilo):
        self._talla = talla
        self._color = color
        self._estilo = estilo

    def get_talla(self):
        return self._talla

    def get_color(self):
        return self._color

    def get_estilo(self):
        return self._estilo

    def set_talla(self, talla):
        self._talla = talla

    def set_color(self, color):
        self._color = color

    def set_estilo(self, estilo):
        self._estilo = estilo

    # EL método __str__ es el método equivalente al ToString de Java y C#
    # Permite escribir el cotenido del objeto
    # Aqui estamos haciendo polimorfismo por sobreescritura
    def __str__(self):
        return f"Talla: {self._talla}, Color: {self._color}, Estilo: {self._estilo}"
