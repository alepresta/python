import psycopg2
from psycopg2 import OperationalError
from typing import Optional, Dict, Any
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

class Conexion:
    _instancia = None

    def __init__(self, config: Dict[str, str]):
        self._config = config
        self._conexion: Optional[psycopg2.extensions.connection] = None
        self._cursor: Optional[psycopg2.extensions.cursor] = None

    @classmethod
    def obtener_conexion(cls, config: Dict[str, str]) -> 'Conexion':
        if cls._instancia is None:
            cls._instancia = cls(config)
            cls._instancia._conectar()
        return cls._instancia

    def _conectar(self) -> None:
        try:
            self._conexion = psycopg2.connect(**self._config)
            self._conexion.autocommit = False
            self._cursor = self._conexion.cursor()
            logger.info("Conexión a la base de datos establecida")
        except OperationalError as e:
            logger.error(f"Error al conectar a la DB: {e}")
            raise

    @contextmanager
    def obtener_cursor(self):
        """Context manager para manejo seguro de cursores"""
        if self._cursor is None or self._conexion.closed:
            self._conectar()

        try:
            yield self._cursor
            self._conexion.commit()
        except Exception as e:
            self._conexion.rollback()
            logger.error(f"Error en transacción: {e}")
            raise

    def cerrar(self) -> None:
        if self._cursor and not self._cursor.closed:
            self._cursor.close()
        if self._conexion and not self._conexion.closed:
            self._conexion.close()
        logger.info("Conexión cerrada")
        Conexion._instancia = None

    def __enter__(self):
        """Implementación del protocolo de administrador de contexto"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Implementación del protocolo de administrador de contexto"""
        self.cerrar()

    def __del__(self):
        self.cerrar()