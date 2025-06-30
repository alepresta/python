import json
import random
import string
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging
import psycopg2
from psycopg2 import sql
from persona import Persona
from persona_dao import PersonaDAO
import config_db  # <-- Añadir esta importación

log = logging.getLogger(__name__)

class GeneradorPersonasCompleto:
    def __init__(self, db_config: Dict[str, str] = None):
        self.base_dir = Path(__file__).parent
        self.datos = self._cargar_datos()
        self.ruta_salida = self.base_dir / "datos_generados" / "ultimas_personas.json"
        self.db_config = db_config
        self._configurar_logging()

    def _configurar_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def _cargar_datos(self) -> Dict[str, List[str]]:
        datos = {}
        carpeta = self.base_dir / "datos_random"

        archivos = {
            "nombres": "nombres.json",
            "apellidos": "apellidos.json",
            "cuits": "cuits.json",
            "codPais": "codPais.json",
            "codRea": "codRea.json",
            "numeroTelefono": "numeroTelefono.json",
            "nacionalidad": "nacionalidad.json"
        }

        for clave, archivo in archivos.items():
            ruta = carpeta / archivo
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    datos[clave] = json.load(f)
            except Exception as e:
                log.error(f"Error cargando {archivo}: {e}")
                raise

        return datos

    def _generar_email(self, nombre: str, apellido: str) -> str:
        """Genera un email aleatorio basado en nombre y apellido"""
        dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "empresa.com"]
        variantes = [
            f"{nombre.lower()}.{apellido.lower()}",
            f"{nombre.lower()[0]}{apellido.lower()}",
            f"{nombre.lower()}{apellido.lower()[0]}",
            f"{nombre.lower()}{random.randint(10, 99)}",
            f"{apellido.lower()}{random.randint(10, 99)}"
        ]
        return f"{random.choice(variantes)}@{random.choice(dominios)}"

    def _generar_dni(self) -> str:
        """Genera un DNI español válido con letra"""
        numero = random.randint(10_000_000, 99_999_999)
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        letra = letras[numero % 23]
        return f"{numero}{letra}"

    def _generar_fecha_nacimiento(self) -> str:
        """Genera una fecha de nacimiento aleatoria (entre 18 y 80 años)"""
        edad = random.randint(18, 80)
        año = datetime.now().year - edad
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)  # Evitamos problemas con meses de 28 días
        return f"{año}-{mes:02d}-{dia:02d}"  # Formato PostgreSQL

    def _generar_password(self) -> str:
        """Genera una contraseña segura con caracteres especiales"""
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(caracteres) for _ in range(12))

    def generar_persona(self) -> Persona:
        sexo = random.choice(["M", "F"])
        nombres = self.datos["nombres"]["hombres"] if sexo == "M" else self.datos["nombres"]["mujeres"]
        nombre = random.choice(nombres)
        apellido = random.choice(self.datos["apellidos"])

        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d")
        horario = ahora.strftime("%H:%M:%S")

        return Persona(
            nombre=nombre,
            apellido=apellido,
            email=self._generar_email(nombre, apellido),
            cuit=random.choice(self.datos["cuits"]),
            sexo="Masculino" if sexo == "M" else "Femenino",
            dni=self._generar_dni(),
            cumple=self._generar_fecha_nacimiento(),
            password=self._generar_password(),
            codigoReserva=f"RES-{random.randint(10000, 99999)}",
            fecha=fecha,
            horario=horario,
            tramite=random.choice(["Licencia", "Pasaporte", "DNI", "Certificado"]),
            puntoAtencion=random.choice(["Centro", "Sucursal", "Oficina"]),
            direccionPuntoAtencion=f"Calle {random.randint(1, 100)} #{random.randint(1, 50)}",
            numeroAfiliado=f"AF-{random.randint(100000, 999999)}",
            codPais=random.choice(self.datos["codPais"]),
            codRea=random.choice(self.datos["codRea"]),
            numeroTelefono=random.choice(self.datos["numeroTelefono"]),
            nacionalidad=random.choice(self.datos["nacionalidad"]),
            numeroTramite=f"TR-{random.randint(10000, 99999)}",
            campoTexto=f"Texto de ejemplo {random.randint(1, 100)}",
            menuDesplegable=random.choice(["Opción 1", "Opción 2", "Opción 3"]),
            areaTexto="Este es un texto de ejemplo para el área de texto.",
            botonOpcion=random.choice(["Si", "No"]),
            campoFecha=fecha,
            organismo=random.choice(["Organismo A", "Organismo B", "Organismo C"]),
            turnoPara=random.choice(["Mi mismo", "Familiar", "Conocido"])
        )

    def generar_personas(self, cantidad: int = 1, insertar_db: bool = False) -> List[Persona]:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        log.info(f"Generando {cantidad} personas ficticias...")
        personas = []

        for _ in range(cantidad):
            persona = self.generar_persona()
            if insertar_db and self.db_config:
                try:
                    persona_insertada = PersonaDAO.insertar(persona)
                    if persona_insertada:
                        personas.append(persona_insertada)
                except Exception as e:
                    log.error(f"No se pudo insertar persona en DB: {e}")
            else:
                personas.append(persona)

        self._guardar_ultimas_personas(personas)
        return personas

    def _guardar_ultimas_personas(self, personas: List[Persona]):
        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        personas_dict = [vars(persona) for persona in personas]

        with open(self.ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(personas_dict, f, ensure_ascii=False, indent=2)

        log.info(f"Últimas {len(personas)} personas guardadas en {self.ruta_salida}")

    def _crear_tabla_si_no_existe(self):
        """Crea la tabla persona si no existe con todas las columnas necesarias"""
        try:
            conn = psycopg2.connect(**self.db_config)
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS persona (
                    id_persona SERIAL PRIMARY KEY,
                    nombre VARCHAR(100),
                    apellido VARCHAR(100),
                    email VARCHAR(100),
                    cuit VARCHAR(20),
                    sexo VARCHAR(10),
                    dni VARCHAR(20),
                    cumple DATE,
                    password VARCHAR(255),
                    codigoReserva VARCHAR(50),
                    fecha DATE,
                    horario TIME,
                    tramite VARCHAR(100),
                    puntoAtencion VARCHAR(100),
                    direccionPuntoAtencion VARCHAR(200),
                    numeroAfiliado VARCHAR(50),
                    codPais VARCHAR(10),
                    codRea VARCHAR(10),
                    numeroTelefono VARCHAR(30),
                    nacionalidad VARCHAR(50),
                    numeroTramite VARCHAR(50),
                    campoTexto TEXT,
                    menuDesplegable VARCHAR(100),
                    areaTexto TEXT,
                    botonOpcion VARCHAR(50),
                    campoFecha DATE,
                    organismo VARCHAR(100),
                    turnoPara VARCHAR(100),
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            conn.commit()
            log.info("Tabla persona verificada/creada exitosamente")

        except Exception as e:
            log.error(f"Error al crear/verificar tabla persona: {e}")
            raise
        finally:
            if conn:
                conn.close()