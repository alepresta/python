from mysql.connector import pooling
from datos_de_la_conexion import DATABASE

class Conexion:
    _pool = None

    @classmethod
    def _inicializar_pool(cls):
        if cls._pool is None:
            cls._pool = pooling.MySQLConnectionPool(
                pool_name=DATABASE['pool_name'],
                pool_size=DATABASE['pool_size'],
                pool_reset_session=DATABASE['pool_reset_session'],
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database'],
                port=DATABASE['port']
            )

    @classmethod
    def conectar(cls):
        if cls._pool is None:
            cls._inicializar_pool()
        return cls._pool.get_connection()