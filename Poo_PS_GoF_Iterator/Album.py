class Album:
    def __init__(self):
        self.lasLaminas = []

    def AgregarLamina(self, lamina):
        self.lasLaminas.append(lamina)

    def __iter__(self):
        self.actual = 0
        return self

    def __next__(self):
        if self.actual < len(self.lasLaminas):
            unaLamina = self.lasLaminas[self.actual]
            self.actual += 1
            return unaLamina
        else:
            raise StopIteration
