class Persona:
    def __init__(self, id_persona: int = None, nombre: str = None,
                 apellido: str = None, email: str = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self) -> str:
        return f"Persona(id={self._id_persona}, nombre={self._nombre}, apellido={self._apellido}, email={self._email})"

    # Propiedades (getters/setters)
    @property
    def id_persona(self) -> int:
        return self._id_persona

    @id_persona.setter
    def id_persona(self, value: int):
        self._id_persona = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, value: str):
        self._apellido = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value