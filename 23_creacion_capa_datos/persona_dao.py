
import logging
from typing import List, Optional
from psycopg2 import sql
from conexion import Conexion
from persona import Persona
import config_db

log = logging.getLogger(__name__)

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = ("INSERT INTO persona (nombre, apellido, email, cuit, sexo, dni, cumple, password, "
                 "codigoReserva, fecha, horario, tramite, puntoAtencion, direccionPuntoAtencion, "
                 "numeroAfiliado, codPais, codRea, numeroTelefono, nacionalidad, numeroTramite, "
                 "campoTexto, menuDesplegable, areaTexto, botonOpcion, campoFecha, organismo, turnoPara) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                 "%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_persona")
    _ACTUALIZAR = ("UPDATE persona SET nombre=%s, apellido=%s, email=%s, cuit=%s, sexo=%s, dni=%s, "
                   "cumple=%s, password=%s, codigoReserva=%s, fecha=%s, horario=%s, tramite=%s, "
                   "puntoAtencion=%s, direccionPuntoAtencion=%s, numeroAfiliado=%s, codPais=%s, "
                   "codRea=%s, numeroTelefono=%s, nacionalidad=%s, numeroTramite=%s, campoTexto=%s, "
                   "menuDesplegable=%s, areaTexto=%s, botonOpcion=%s, campoFecha=%s, organismo=%s, "
                   "turnoPara=%s WHERE id_persona=%s")
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"
    _SELECCIONAR_ID = "SELECT * FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls) -> List[Persona]:
        conexion = Conexion.obtener_conexion(config_db.DATABASE)
        cursor = conexion._cursor
        try:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(
                    id_persona=registro[0],
                    nombre=registro[1],
                    apellido=registro[2],
                    email=registro[3],
                    cuit=registro[4],
                    sexo=registro[5],
                    dni=registro[6],
                    cumple=registro[7],
                    password=registro[8],
                    codigoReserva=registro[9],
                    fecha=registro[10],
                    horario=registro[11],
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
                    campoFecha=registro[25],
                    organismo=registro[26],
                    turnoPara=registro[27]
                )
                personas.append(persona)
            return personas
        except Exception as e:
            log.error(f"Error al seleccionar personas: {e}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertar(cls, persona: Persona) -> Optional[Persona]:
        conexion = Conexion.obtener_conexion(config_db.DATABASE)
        cursor = conexion._cursor
        try:
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
            conexion._conexion.commit()
            log.info(f"Persona insertada: {persona}")
            return persona
        except Exception as e:
            conexion._conexion.rollback()
            log.error(f"Error al insertar persona: {e}")
            return None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizar(cls, persona: Persona) -> Optional[Persona]:
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
                    persona.turnoPara, persona.id_persona
                )
                cursor.execute(cls._ACTUALIZAR, valores)
                log.info(f"Persona actualizada: {persona}")
                return persona

    @classmethod
    def eliminar(cls, persona: Persona) -> bool:
        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (persona.id_persona,))
                log.info(f"Persona eliminada: {persona}")
                return True

    @classmethod
    def seleccionar_por_id(cls, id_persona: int) -> Optional[Persona]:
        with Conexion.obtener_conexion(config_db.DATABASE) as conexion:
            with conexion.obtener_cursor() as cursor:
                cursor.execute(cls._SELECCIONAR_ID, (id_persona,))
                registro = cursor.fetchone()
                if registro:
                    return Persona(
                        id_persona=registro[0],
                        nombre=registro[1],
                        apellido=registro[2],
                        email=registro[3],
                        # ... completar con todos los campos
                    )
                return None