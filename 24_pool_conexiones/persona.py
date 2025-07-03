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
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cuit = cuit
        self.sexo = sexo
        self.dni = dni
        self.cumple = cumple
        self.password = password
        self.codigoReserva = codigoReserva
        self.fecha = fecha
        self.horario = horario
        self.tramite = tramite
        self.puntoAtencion = puntoAtencion
        self.direccionPuntoAtencion = direccionPuntoAtencion
        self.numeroAfiliado = numeroAfiliado
        self.codPais = codPais
        self.codRea = codRea
        self.numeroTelefono = numeroTelefono
        self.nacionalidad = nacionalidad
        self.numeroTramite = numeroTramite
        self.campoTexto = campoTexto
        self.menuDesplegable = menuDesplegable
        self.areaTexto = areaTexto
        self.botonOpcion = botonOpcion
        self.campoFecha = campoFecha
        self.organismo = organismo
        self.turnoPara = turnoPara

    def __str__(self) -> str:
        return (f"Persona(id={self.id_persona}, nombre={self.nombre}, apellido={self.apellido}, "
                f"email={self.email}, dni={self.dni})")

    def __repr__(self) -> str:
        return self.__str__()
