from mysql.connector import pooling
from datos_de_la_conexion import DATABASE
from mysql.connector import Error

class Conexion:
    _pool = None

    @classmethod
    def _inicializar_pool(cls):
        if cls._pool is None:
            try:
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
                #print(f'Nombre del pool: {cls._pool.pool_name}')
                #print(f'Tamaño del pool: {cls._pool.pool_size}')
                return  cls._pool
            except Error as e:
                print(f'Ocurrio un error al obtener el pool: {e}')

    @classmethod
    def conectar(cls):
        if cls._pool is None:
            cls._inicializar_pool()
        return cls._pool.get_connection()

    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()

