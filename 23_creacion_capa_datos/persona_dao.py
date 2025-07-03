import logging
from typing import List, Optional
from conexion import Conexion
from persona import Persona
import config_db

log = logging.getLogger(__name__)


class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = (
        "INSERT INTO persona (nombre, apellido, email, cuit, sexo, dni, cumple, password, "
        "codigoReserva, fecha, horario, tramite, puntoAtencion, direccionPuntoAtencion, "
        "numeroAfiliado, codPais, codRea, numeroTelefono, nacionalidad, numeroTramite, "
        "campoTexto, menuDesplegable, areaTexto, botonOpcion, campoFecha, organismo, turnoPara) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
        "%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_persona"
    )
    _ACTUALIZAR = (
        "UPDATE persona SET nombre=%s, apellido=%s, email=%s, cuit=%s, sexo=%s, dni=%s, "
        "cumple=%s, password=%s, codigoReserva=%s, fecha=%s, horario=%s, tramite=%s, "
        "puntoAtencion=%s, direccionPuntoAtencion=%s, numeroAfiliado=%s, codPais=%s, "
        "codRea=%s, numeroTelefono=%s, nacionalidad=%s, numeroTramite=%s, campoTexto=%s, "
        "menuDesplegable=%s, areaTexto=%s, botonOpcion=%s, campoFecha=%s, organismo=%s, "
        "turnoPara=%s WHERE id_persona=%s"
    )
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"
    _SELECCIONAR_ID = "SELECT * FROM persona WHERE id_persona=%s"

    @classmethod
    def obtener_todos(cls, limit: int = 100) -> List[Persona]:
        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                cursor.execute(f"{cls._SELECCIONAR} LIMIT %s", (limit,))
                registros = cursor.fetchall()
                personas = [cls._registro_a_persona(r) for r in registros]
                return personas

    @classmethod
    def insertar(cls, persona: Persona) -> Optional[Persona]:
        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                valores = (
                    persona.nombre, persona.apellido, persona.email, persona.cuit, persona.sexo,
                    persona.dni, persona.cumple, persona.password, persona.codigoReserva,
                    persona.fecha, persona.horario, persona.tramite, persona.puntoAtencion,
                    persona.direccionPuntoAtencion, persona.numeroAfiliado, persona.codPais,
                    persona.codRea, persona.numeroTelefono, persona.nacionalidad,
                    persona.numeroTramite, persona.campoTexto, persona.menuDesplegable,
                    persona.areaTexto, persona.botonOpcion, persona.campoFecha, persona.organismo,
                    persona.turnoPara
                )
                cursor.execute(cls._INSERTAR, valores)
                persona.id_persona = cursor.fetchone()[0]
                log.info(f"Persona insertada: {persona}")
                return persona

    @classmethod
    def actualizar(cls, id_persona: int, nuevos_valores: dict) -> Optional[Persona]:
        campos = list(nuevos_valores.keys())
        valores = [nuevos_valores[c] for c in campos]
        valores.append(id_persona)

        placeholders = ", ".join([f"{campo}=%s" for campo in campos])
        query = f"UPDATE persona SET {placeholders} WHERE id_persona=%s"

        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                cursor.execute(query, valores)
                log.info(f"Persona actualizada ID={id_persona}")
                return cls.obtener_por_id(id_persona)

    @classmethod
    def eliminar(cls, id_persona: int) -> bool:
        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (id_persona,))
                log.info(f"Persona eliminada ID={id_persona}")
                return True

    @classmethod
    def obtener_por_id(cls, id_persona: int) -> Optional[Persona]:
        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                cursor.execute(cls._SELECCIONAR_ID, (id_persona,))
                registro = cursor.fetchone()
                if registro:
                    return cls._registro_a_persona(registro)
                return None

    @staticmethod
    def _registro_a_persona(registro) -> Persona:
        return Persona(
            id_persona=registro[0],
            nombre=registro[1],
            apellido=registro[2],
            email=registro[3],
            cuit=registro[4],
            sexo=registro[5],
            dni=registro[6],
            cumple=str(registro[7]),
            password=registro[8],
            codigoReserva=registro[9],
            fecha=str(registro[10]),
            horario=str(registro[11]),
            tramite=registro[12],
            puntoAtencion=registro[13],
            direccionPuntoAtencion=registro[14],
            numeroAfiliado=registro[15],
            codPais=registro[16],
            codRea=registro[17],
            numeroTelefono=registro[18],
            nacionalidad=registro[19],
            numeroTramite=registro[20],
            campoTexto=registro[21],
            menuDesplegable=registro[22],
            areaTexto=registro[23],
            botonOpcion=registro[24],
            campoFecha=str(registro[25]),
            organismo=registro[26],
            turnoPara=registro[27]
        )
