import psycopg2
from psycopg2 import pool
import sys
import logger_base as log

class Conexion:
    DATABASE = 'test_db'
    USERNAME = 'apresta'
    PASSWORD = 'miamigodardo1pa'
    DB_PORT = '5432'
    HOST = '85.31.224.145'
    MIN_CON = 1
    MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls.MIN_CON, cls.MAX_CON,
                    host=cls.HOST,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    port=cls.DB_PORT,
                    database=cls.DATABASE
                )
                #log.logger.debug("Pool de conexiones creado correctamente.")
            except Exception as e:
                log.logger.error(f"Error al crear el pool de conexiones: {e}")
                sys.exit()
        return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        #log.logger.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        #log.logger.debug(f"Conexión regresada al pool: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        #log.logger.debug("Conexiones del pool cerradas.")
