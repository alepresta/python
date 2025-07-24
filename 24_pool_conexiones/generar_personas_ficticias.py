import json
import random
import string
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

from persona import Persona
from persona_dao import PersonaDAO
from conexion import ConexionPool  # Cambiado
import config_db

log = logging.getLogger(__name__)


class GeneradorPersonasCompleto:
    def __init__(self, db_config: Dict[str, str] = None):
        self.base_dir = Path(__file__).parent
        self.ruta_salida = self.base_dir / "datos_generados" / "ultimas_personas.json"
        self.db_config = db_config or config_db.DATABASE
        self.datos = self._cargar_datos()
        self._crear_tabla_si_no_existe()

    def _cargar_datos(self) -> Dict[str, Any]:
        datos = {}
        carpeta = self.base_dir / "datos_random"

        archivos = {
            "nombres": "nombres.json",
            "apellidos": "apellidos.json",
            "cuits": "cuits.json",
            "codPais": "codPais.json",
            "codRea": "codRea.json",
            "numeroTelefono": "numeroTelefono.json",
            "nacionalidad": "nacionalidad.json",
            "tramites": "tramites.json",
            "puntos_atencion": "puntos_atencion.json",
            "organismos": "organismos.json"
        }

        for clave, archivo in archivos.items():
            ruta = carpeta / archivo
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    datos[clave] = json.load(f)
            except Exception as e:
                log.error(f"Error cargando {archivo}: {e}")
                raise RuntimeError(f"No se pudo cargar el archivo {archivo}") from e

        return datos

    def _generar_email(self, nombre: str, apellido: str) -> str:
        dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "empresa.com"]
        variantes = [
            f"{nombre.lower()}.{apellido.lower()}",
            f"{nombre.lower()[0]}{apellido.lower()}",
            f"{nombre.lower()}{apellido.lower()[0]}",
            f"{nombre.lower()}{random.randint(10, 99)}",
            f"{apellido.lower()}{random.randint(10, 99)}"
        ]
        return f"{random.choice(variantes)}@{random.choice(dominios)}"

    def _generar_dni_from_cuit(self, cuit: str) -> str:
        if len(cuit) != 11 or not cuit.isdigit():
            raise ValueError(f"CUIT inválido: {cuit}")
        return cuit[2:10].zfill(8)

    def _generar_fecha_nacimiento(self) -> str:
        edad = random.randint(18, 80)
        fecha = datetime.now().replace(year=datetime.now().year - edad)
        dia = random.randint(1, 28)
        mes = random.randint(1, 12)
        return f"{fecha.year}-{mes:02d}-{dia:02d}"

    def _generar_password(self) -> str:
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(caracteres) for _ in range(12))

    def _generar_telefono_valido(self, nacionalidad: str) -> Dict[str, str]:
        es_argentino = "argentino" in nacionalidad.lower()
        cod_pais = "+54" if es_argentino else random.choice(self.datos["codPais"])

        if cod_pais == "+54":
            cod_rea = random.choice(["11", "221", "341", "261"])
            numero = "15" + ''.join(random.choices(string.digits, k=6))
        else:
            cod_rea = "".join(random.choices(string.digits, k=random.randint(1, 4)))
            numero = ''.join(random.choices(string.digits, k=7))

        return {
            "codPais": cod_pais,
            "codRea": cod_rea,
            "numeroTelefono": numero
        }

    def _seleccionar_tramite(self) -> Dict[str, Any]:
        tramite = random.choice(self.datos["tramites"])
        return {
            "id": tramite[0],
            "nombre": tramite[1],
            "ambiente": tramite[2]
        }

    def _seleccionar_punto_atencion(self, ambiente: str) -> Dict[str, str]:
        puntos = self.datos["puntos_atencion"].get(ambiente, []) or self.datos["puntos_atencion"].get("qa", [])
        punto = random.choice(puntos)
        return {
            "id": punto["id"],
            "nombre": punto["nombre"],
            "direccion": punto["direccion"]
        }

    def generar_persona(self) -> Persona:
        sexo = random.choice(["M", "F", "X"])
        nombres = self.datos["nombres"][
            "hombres" if sexo == "M" else
            "mujeres" if sexo == "F" else
            "genero_x"
        ]
        nombre = random.choice(nombres)
        apellido = random.choice(self.datos["apellidos"])
        nacionalidad = random.choice(self.datos["nacionalidad"])
        cuit = random.choice(self.datos["cuits"])
        dni = self._generar_dni_from_cuit(cuit)
        ahora = datetime.now()
        telefono = self._generar_telefono_valido(nacionalidad)
        tramite = self._seleccionar_tramite()
        punto = self._seleccionar_punto_atencion(tramite["ambiente"])

        return Persona(
            nombre=nombre,
            apellido=apellido,
            email=self._generar_email(nombre, apellido),
            cuit=cuit,
            sexo = "Masculino" if sexo == "M" else "Femenino" if sexo == "F" else "No binario" if sexo == "X" else sexo,
            dni=dni,
            cumple=self._generar_fecha_nacimiento(),
            password=self._generar_password(),
            codigoReserva=f"RES-{random.randint(10000, 99999)}",
            fecha=ahora.strftime("%Y-%m-%d"),
            horario=ahora.strftime("%H:%M:%S"),
            tramite=tramite["nombre"],
            puntoAtencion=punto["nombre"],
            direccionPuntoAtencion=punto["direccion"],
            numeroAfiliado=f"AF-{random.randint(100000, 999999)}",
            codPais=telefono["codPais"],
            codRea=telefono["codRea"],
            numeroTelefono=telefono["numeroTelefono"],
            nacionalidad=nacionalidad,
            numeroTramite=f"TR-{random.randint(10000, 99999)}",
            campoTexto=f"Texto de ejemplo {random.randint(1, 100)}",
            menuDesplegable=random.choice(["Opción 1", "Opción 2", "Opción 3"]),
            areaTexto="Texto de ejemplo para el área de texto.",
            botonOpcion=random.choice(["Sí", "No"]),
            campoFecha=ahora.strftime("%Y-%m-%d"),
            organismo=random.choice(self.datos["organismos"]),
            turnoPara=random.choice(["Mi mismo", "Familiar", "Conocido"])
        )

    def generar_personas(self, cantidad: int = 1, insertar_db: bool = False) -> List[Persona]:
        personas = []
        for _ in range(cantidad):
            persona = self.generar_persona()
            if insertar_db:
                try:
                    persona_insertada = PersonaDAO.insertar(persona)
                    if persona_insertada:
                        personas.append(persona_insertada)
                except Exception as e:
                    log.error(f"No se pudo insertar persona: {e}")
            else:
                personas.append(persona)

        self._guardar_ultimas_personas(personas)
        return personas

    def _guardar_ultimas_personas(self, personas: List[Persona]):
        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ruta_salida, 'w', encoding='utf-8') as f:
            json.dump([vars(p) for p in personas], f, ensure_ascii=False, indent=2)
        log.info(f"{len(personas)} personas guardadas en {self.ruta_salida}")

    def _crear_tabla_si_no_existe(self):
        sql = """
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
        """
        try:
            pool = ConexionPool.obtener_pool(self.db_config)
            with pool.obtener_cursor() as cursor:
                cursor.execute(sql)
                log.info("Tabla persona verificada/creada")
        except Exception as e:
            log.error(f"Error creando/verificando tabla persona: {e}")


import sys
from persona import Persona
from persona_dao import PersonaDAO
from conexion import ConexionPool  # Cambiado

class SistemaGestionPersonas:
    def __init__(self):
        self.generador = GeneradorPersonasCompleto()

    def menu_principal(self):
        while True:
            opcion = self._mostrar_menu()

            if opcion == 1:
                self.generar_personas_automaticamente()
            elif opcion == 2:
                self.crear_persona_manual()
            elif opcion == 3:
                self.listar_personas()
            elif opcion == 4:
                self.buscar_persona_por_id()
            elif opcion == 5:
                self.editar_persona_por_id()
            elif opcion == 6:
                self.eliminar_persona_por_id()
            elif opcion == 7:
                self.eliminar_todos_datos()
            elif opcion == 8:
                print("Saliendo del sistema.")
                break

    def _mostrar_menu(self):
        print("\n=== SISTEMA DE GESTIÓN DE PERSONAS ===")
        print("1. Generar personas automáticamente")
        print("2. Crear persona manualmente")
        print("3. Listar personas")
        print("4. Buscar persona por ID")
        print("5. Editar persona")
        print("6. Eliminar persona")
        print("7. Eliminar todos los datos")
        print("8. Salir")
        while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= 8:
                    return opcion
            except ValueError:
                pass
            print("Opción inválida, intente de nuevo.")

    def _obtener_input(self, mensaje, tipo=str, default=None):
        while True:
            entrada = input(f"{mensaje} [{default}]: ") if default is not None else input(f"{mensaje}: ")

            if entrada.strip().lower() in ['null', 'none']:
                return None
            if not entrada.strip() and default is not None:
                return default
            if not entrada.strip():
                print("Este campo es obligatorio.")
                continue

            try:
                return tipo(entrada)
            except ValueError:
                print(f"Entrada inválida. Se esperaba tipo {tipo.__name__}")


    def generar_personas_automaticamente(self):
        cantidad = self._obtener_input("¿Cuántas personas desea generar?", int, 1)
        personas = self.generador.generar_personas(cantidad, insertar_db=True)
        print(f"Se generaron {len(personas)} personas.")

    def crear_persona_manual(self):
        base = self.generador.generar_persona()
        datos = vars(base)
        for campo in datos:
            valor = self._obtener_input(f"Ingrese {campo}", str, datos[campo])
            datos[campo] = valor
        persona = Persona(**datos)
        PersonaDAO.insertar(persona)
        print("Persona creada.")

    def listar_personas(self):
        personas = PersonaDAO.obtener_todos(limit=50)
        for p in personas:
            print(f"[{p.id_persona}] {p.nombre} {p.apellido} - CUIT: {p.cuit}")

    def buscar_persona_por_id(self):
        pid = self._obtener_input("ID de la persona", int)
        persona = PersonaDAO.obtener_por_id(pid)
        if persona:
            self._mostrar_detalle(persona)
        else:
            print("No se encontró la persona.")

    def editar_persona_por_id(self):
        pid = self._obtener_input("ID de la persona", int)
        persona = PersonaDAO.obtener_por_id(pid)
        if not persona:
            print("No se encontró la persona.")
            return
        datos = vars(persona)
        nuevos = {}
        for campo, valor in datos.items():
            if campo == 'id_persona':
                continue
            nuevo = self._obtener_input(f"{campo}", str, valor)
            nuevos[campo] = nuevo
        PersonaDAO.actualizar(pid, nuevos)
        print("Persona actualizada.")

    def eliminar_persona_por_id(self):
        pid = self._obtener_input("ID de la persona", int)
        if PersonaDAO.eliminar(pid):
            print("Persona eliminada.")

    def eliminar_todos_datos(self):
        confirmar = input("¿Está seguro de eliminar TODOS los datos? (si/no): ").lower()
        if confirmar == "si":
            pool = ConexionPool.obtener_pool(config_db.DATABASE)
            with pool.obtener_cursor() as cursor:
                cursor.execute("TRUNCATE persona RESTART IDENTITY CASCADE")
                print("Todos los datos han sido eliminados.")

    def _mostrar_detalle(self, persona: Persona):
        print("\n=== DETALLE DE PERSONA ===")
        for campo, valor in vars(persona).items():
            print(f"{campo}: {valor}")