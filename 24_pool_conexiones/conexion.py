import psycopg2
from psycopg2 import OperationalError
from typing import Optional, Dict, Any
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)


class Conexion:
    _instancias: Dict[str, 'Conexion'] = {}

    def __init__(self, config: Dict[str, str]):
        self._config = config
        self._conexion: Optional[psycopg2.extensions.connection] = None

    @classmethod
    def obtener_conexion(cls, config: Dict[str, str]) -> 'Conexion':
        clave = f"{config.get('host')}:{config.get('port')}:{config.get('dbname')}:{config.get('user')}"
        if clave not in cls._instancias:
            instancia = cls(config)
            instancia._conectar()
            cls._instancias[clave] = instancia
        return cls._instancias[clave]

    def _conectar(self) -> None:
        try:
            self._conexion = psycopg2.connect(**self._config)
            self._conexion.autocommit = False
            logger.info("Conexión a la base de datos establecida")
        except OperationalError as e:
            logger.error(f"Error al conectar a la DB: {e}")
            raise

    @contextmanager
    def obtener_cursor(self):
        """Context manager para manejo seguro de cursores"""
        if self._conexion is None or self._conexion.closed:
            self._conectar()

        cursor = self._conexion.cursor()
        try:
            yield cursor
            self._conexion.commit()
        except Exception as e:
            self._conexion.rollback()
            logger.error(f"Error en transacción: {e}")
            raise
        finally:
            cursor.close()

    def cerrar(self) -> None:
        if self._conexion and not self._conexion.closed:
            self._conexion.close()
            logger.info("Conexión cerrada")
        # Eliminar la instancia del pool
        claves_a_borrar = [k for k, v in self._instancias.items() if v is self]
        for k in claves_a_borrar:
            del self._instancias[k]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar()
