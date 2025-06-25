from conexion import Conexion
from persona import Persona


class PersonaDAO:
    SELECCIONAR = "SELECT id_persona, nombre, apellido, email FROM persona"
    INSERTAR = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s) RETURNING id_persona"
    ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls, id_persona: int = None) -> list[Persona]:
        query = cls.SELECCIONAR
        params = None

        if id_persona:
            query += " WHERE id_persona = %s"
            params = (id_persona,)

        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return [Persona(id_persona=row[0], nombre=row[1], apellido=row[2], email=row[3]) for row in resultados]
        except Exception as e:
            print(f"Error al seleccionar personas: {e}")
            return []

    @classmethod
    def insertar(cls, persona: Persona) -> Persona:
        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(cls.INSERTAR, (persona.nombre, persona.apellido, persona.email))
            id_generado = cursor.fetchone()[0]
            Conexion._instancia._conexion.commit()  # Accedemos directamente a la instancia Singleton
            persona.id_persona = id_generado
            return persona
        except Exception as e:
            print(f"Error al insertar persona: {e}")
            Conexion._instancia._conexion.rollback()
            return None

    @classmethod
    def actualizar(cls, persona: Persona) -> bool:
        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(cls.ACTUALIZAR, (persona.nombre, persona.apellido, persona.email, persona.id_persona))
            Conexion._instancia._conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar persona: {e}")
            Conexion._instancia._conexion.rollback()
            return False

    @classmethod
    def eliminar(cls, id_persona: int) -> bool:
        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(cls.ELIMINAR, (id_persona,))
            Conexion._instancia._conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar persona: {e}")
            Conexion._instancia._conexion.rollback()
            return False