class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre.strip().title()