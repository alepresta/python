class Cliente:
    def __init__(self,nombre=None,apellido=None,membresia=None,id=None):
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
        self._nombre = str(nombre).strip().title() if nombre is not None else None

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = str(apellido).strip().title() if apellido is not None else None

    @property
    def membresia(self):
        return self._membresia

    @membresia.setter
    def membresia(self,membresia):
        self._membresia = str(membresia).strip().title() if membresia is not None else None

    @property
    def id(self):
        return  self._id

    @id.setter
    def id(self,id):
        self._id = str(id).strip() if id is not None else None

