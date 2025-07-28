class Cliente:
    def __init__(self,nombre,apellido,membresia,id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
        self.id = id

    def __str__(self):
        return f'{self._nombre}, {self._apellido}, {self._membresia}, {self._id}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre.strip().title()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido.strip().title()

    @property
    def membresia(self):
        return self._membresia

    @membresia.setter
    def membresia(self,membresia):
        self._membresia = membresia.strip().title()

    @property
    def id(self):
        return  self._id

    @id.setter
    def id(self,id):
        self._id = id

