import psycopg2
from psycopg2 import pool, OperationalError
from typing import Optional, Dict, Any, List
from contextlib import contextmanager
import logging
from threading import Lock

logger = logging.getLogger(__name__)


class ConexionPool:
    _instancias: Dict[str, 'ConexionPool'] = {}
    _lock = Lock()
    _MAX_CONEXIONES = 5
    _MIN_CONEXIONES = 1  # Puedes ajustar este valor según necesites

    def __init__(self, config: Dict[str, str]):
        self._config = config
        self._connection_pool: Optional[psycopg2.pool.SimpleConnectionPool] = None
        self._initialize_pool()

    def _initialize_pool(self):
        try:
            self._connection_pool = psycopg2.pool.SimpleConnectionPool(
                minconn=self._MIN_CONEXIONES,
                maxconn=self._MAX_CONEXIONES,
                **self._config
            )
            logger.info("Pool de conexiones inicializado")
        except OperationalError as e:
            logger.error(f"Error al crear el pool de conexiones: {e}")
            raise

    @classmethod
    def obtener_pool(cls, config: Dict[str, str]) -> 'ConexionPool':
        clave = f"{config.get('host')}:{config.get('port')}:{config.get('dbname')}:{config.get('user')}"
        with cls._lock:
            if clave not in cls._instancias:
                cls._instancias[clave] = cls(config)
            return cls._instancias[clave]

    @contextmanager
    def obtener_conexion(self):
        """Context manager para obtener una conexión del pool"""
        if self._connection_pool is None:
            self._initialize_pool()

        conexion = self._connection_pool.getconn()
        try:
            yield conexion
        except Exception as e:
            logger.error(f"Error durante el uso de la conexión: {e}")
            raise
        finally:
            if conexion and not conexion.closed:
                self._connection_pool.putconn(conexion)

    @contextmanager
    def obtener_cursor(self):
        """Context manager para manejo seguro de cursores"""
        with self.obtener_conexion() as conexion:
            cursor = conexion.cursor()
            try:
                yield cursor
                conexion.commit()
            except Exception as e:
                conexion.rollback()
                logger.error(f"Error en transacción: {e}")
                raise
            finally:
                cursor.close()

    def cerrar_todo(self) -> None:
        """Cierra todas las conexiones del pool"""
        if self._connection_pool:
            self._connection_pool.closeall()
            logger.info("Todas las conexiones del pool cerradas")
        # Eliminar la instancia del pool
        claves_a_borrar = [k for k, v in self._instancias.items() if v is self]
        for k in claves_a_borrar:
            del self._instancias[k]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar_todo()