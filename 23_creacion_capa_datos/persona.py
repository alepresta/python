import logging
from typing import Optional

log = logging.getLogger(__name__)


class Persona:
    def __init__(self,
                 id_persona: Optional[int] = None,
                 nombre: Optional[str] = None,
                 apellido: Optional[str] = None,
                 email: Optional[str] = None,
                 cuit: Optional[str] = None,
                 sexo: Optional[str] = None,
                 dni: Optional[str] = None,
                 cumple: Optional[str] = None,
                 password: Optional[str] = None,
                 codigoReserva: Optional[str] = None,
                 fecha: Optional[str] = None,
                 horario: Optional[str] = None,
                 tramite: Optional[str] = None,
                 puntoAtencion: Optional[str] = None,
                 direccionPuntoAtencion: Optional[str] = None,
                 numeroAfiliado: Optional[str] = None,
                 codPais: Optional[str] = None,
                 codRea: Optional[str] = None,
                 numeroTelefono: Optional[str] = None,
                 nacionalidad: Optional[str] = None,
                 numeroTramite: Optional[str] = None,
                 campoTexto: Optional[str] = None,
                 menuDesplegable: Optional[str] = None,
                 areaTexto: Optional[str] = None,
                 botonOpcion: Optional[str] = None,
                 campoFecha: Optional[str] = None,
                 organismo: Optional[str] = None,
                 turnoPara: Optional[str] = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._cuit = cuit
        self._sexo = sexo
        self._dni = dni
        self._cumple = cumple
        self._password = password
        self._codigoReserva = codigoReserva
        self._fecha = fecha
        self._horario = horario
        self._tramite = tramite
        self._puntoAtencion = puntoAtencion
        self._direccionPuntoAtencion = direccionPuntoAtencion
        self._numeroAfiliado = numeroAfiliado
        self._codPais = codPais
        self._codRea = codRea
        self._numeroTelefono = numeroTelefono
        self._nacionalidad = nacionalidad
        self._numeroTramite = numeroTramite
        self._campoTexto = campoTexto
        self._menuDesplegable = menuDesplegable
        self._areaTexto = areaTexto
        self._botonOpcion = botonOpcion
        self._campoFecha = campoFecha
        self._organismo = organismo
        self._turnoPara = turnoPara

    def __str__(self) -> str:
        return (f"Persona(id={self._id_persona}, nombre={self._nombre}, apellido={self._apellido}, "
                f"email={self._email}, dni={self._dni})")

    # Propiedades (getters/setters)
    @property
    def id_persona(self) -> Optional[int]:
        return self._id_persona

    @id_persona.setter
    def id_persona(self, value: Optional[int]):
        self._id_persona = value

    @property
    def nombre(self) -> Optional[str]:
        return self._nombre

    @nombre.setter
    def nombre(self, value: Optional[str]):
        self._nombre = value

    @property
    def apellido(self) -> Optional[str]:
        return self._apellido

    @apellido.setter
    def apellido(self, value: Optional[str]):
        self._apellido = value

    @property
    def email(self) -> Optional[str]:
        return self._email

    @email.setter
    def email(self, value: Optional[str]):
        self._email = value

    @property
    def cuit(self) -> Optional[str]:
        return self._cuit

    @cuit.setter
    def cuit(self, value: Optional[str]):
        self._cuit = value

    @property
    def sexo(self) -> Optional[str]:
        return self._sexo

    @sexo.setter
    def sexo(self, value: Optional[str]):
        self._sexo = value

    @property
    def dni(self) -> Optional[str]:
        return self._dni

    @dni.setter
    def dni(self, value: Optional[str]):
        self._dni = value

    @property
    def cumple(self) -> Optional[str]:
        return self._cumple

    @cumple.setter
    def cumple(self, value: Optional[str]):
        self._cumple = value

    @property
    def password(self) -> Optional[str]:
        return self._password

    @password.setter
    def password(self, value: Optional[str]):
        self._password = value

    @property
    def codigoReserva(self) -> Optional[str]:
        return self._codigoReserva

    @codigoReserva.setter
    def codigoReserva(self, value: Optional[str]):
        self._codigoReserva = value

    @property
    def fecha(self) -> Optional[str]:
        return self._fecha

    @fecha.setter
    def fecha(self, value: Optional[str]):
        self._fecha = value

    @property
    def horario(self) -> Optional[str]:
        return self._horario

    @horario.setter
    def horario(self, value: Optional[str]):
        self._horario = value

    @property
    def tramite(self) -> Optional[str]:
        return self._tramite

    @tramite.setter
    def tramite(self, value: Optional[str]):
        self._tramite = value

    @property
    def puntoAtencion(self) -> Optional[str]:
        return self._puntoAtencion

    @puntoAtencion.setter
    def puntoAtencion(self, value: Optional[str]):
        self._puntoAtencion = value

    @property
    def direccionPuntoAtencion(self) -> Optional[str]:
        return self._direccionPuntoAtencion

    @direccionPuntoAtencion.setter
    def direccionPuntoAtencion(self, value: Optional[str]):
        self._direccionPuntoAtencion = value

    @property
    def numeroAfiliado(self) -> Optional[str]:
        return self._numeroAfiliado

    @numeroAfiliado.setter
    def numeroAfiliado(self, value: Optional[str]):
        self._numeroAfiliado = value

    @property
    def codPais(self) -> Optional[str]:
        return self._codPais

    @codPais.setter
    def codPais(self, value: Optional[str]):
        self._codPais = value

    @property
    def codRea(self) -> Optional[str]:
        return self._codRea

    @codRea.setter
    def codRea(self, value: Optional[str]):
        self._codRea = value

    @property
    def numeroTelefono(self) -> Optional[str]:
        return self._numeroTelefono

    @numeroTelefono.setter
    def numeroTelefono(self, value: Optional[str]):
        self._numeroTelefono = value

    @property
    def nacionalidad(self) -> Optional[str]:
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, value: Optional[str]):
        self._nacionalidad = value

    @property
    def numeroTramite(self) -> Optional[str]:
        return self._numeroTramite

    @numeroTramite.setter
    def numeroTramite(self, value: Optional[str]):
        self._numeroTramite = value

    @property
    def campoTexto(self) -> Optional[str]:
        return self._campoTexto

    @campoTexto.setter
    def campoTexto(self, value: Optional[str]):
        self._campoTexto = value

    @property
    def menuDesplegable(self) -> Optional[str]:
        return self._menuDesplegable

    @menuDesplegable.setter
    def menuDesplegable(self, value: Optional[str]):
        self._menuDesplegable = value

    @property
    def areaTexto(self) -> Optional[str]:
        return self._areaTexto

    @areaTexto.setter
    def areaTexto(self, value: Optional[str]):
        self._areaTexto = value

    @property
    def botonOpcion(self) -> Optional[str]:
        return self._botonOpcion

    @botonOpcion.setter
    def botonOpcion(self, value: Optional[str]):
        self._botonOpcion = value

    @property
    def campoFecha(self) -> Optional[str]:
        return self._campoFecha

    @campoFecha.setter
    def campoFecha(self, value: Optional[str]):
        self._campoFecha = value

    @property
    def organismo(self) -> Optional[str]:
        return self._organismo

    @organismo.setter
    def organismo(self, value: Optional[str]):
        self._organismo = value

    @property
    def turnoPara(self) -> Optional[str]:
        return self._turnoPara

    @turnoPara.setter
    def turnoPara(self, value: Optional[str]):
        self._turnoPara = value