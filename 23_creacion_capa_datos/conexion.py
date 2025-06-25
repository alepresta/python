import psycopg2
from psycopg2 import OperationalError
from typing import Optional, List, Dict, Any


class Conexion:
    _instancia = None  # Para implementar Singleton

    def __init__(self, database: str, username: str, password: str, db_port: str, host: str):
        self._database = database
        self._username = username
        self._password = password
        self._db_port = db_port
        self._host = host
        self._conexion: Optional[psycopg2.extensions.connection] = None
        self._cursor: Optional[psycopg2.extensions.cursor] = None

    @classmethod
    def obtener_conexion(cls, config: Dict[str, str]) -> 'Conexion':
        """Implementa patrón Singleton para la conexión"""
        if cls._instancia is None:
            cls._instancia = cls(
                database=config['database'],
                username=config['username'],
                password=config['password'],
                db_port=config['db_port'],
                host=config['host']
            )
            cls._instancia._conectar()
        return cls._instancia

    def _conectar(self) -> None:
        """Establece la conexión y el cursor"""
        try:
            self._conexion = psycopg2.connect(
                database=self._database,
                user=self._username,
                password=self._password,
                host=self._host,
                port=self._db_port
            )
            self._cursor = self._conexion.cursor()
        except OperationalError as e:
            raise Exception(f"Error al conectar a la DB: {e}")

    @classmethod
    def obtener_cursor(cls) -> psycopg2.extensions.cursor:
        """Devuelve el cursor activo"""
        if cls._instancia is None:
            raise Exception("Primero debe obtener una conexión")
        if cls._instancia._cursor is None or cls._instancia._conexion.closed:
            cls._instancia._conectar()
        return cls._instancia._cursor

    @classmethod
    def cerrar(cls) -> None:  # Había un error tipográfico (cerar)
        """Cierra la conexión y el cursor"""
        if cls._instancia:
            if cls._instancia._cursor and not cls._instancia._cursor.closed:
                cls._instancia._cursor.close()
            if cls._instancia._conexion and not cls._instancia._conexion.closed:
                cls._instancia._conexion.close()
            cls._instancia = None

    def __del__(self):
        """Destructor para asegurar que se cierra la conexión"""
        self.cerrar()












