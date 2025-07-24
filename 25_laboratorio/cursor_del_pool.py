from conexion import Conexion
import logger_base as log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        if valor_excepcion:
            self._conexion.rollback()
            log.logger.error("Se hizo rollback por excepción")
        else:
            self._conexion.commit()
            #log.logger.debug("Commit realizado")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
