#!/usr/bin/env python3
# ejemplo_uso.py - Ejemplo de uso del sistema de gestión de personas ficticias

from generar_personas_ficticias import SistemaGestionPersonas
from logger_base import configurar_logging
import logging

def main():
    logger = configurar_logging()
    logger.info("Inicio del sistema")

    try:
        sistema = SistemaGestionPersonas()
        print("\nBienvenido al Sistema de Gestión de Personas Ficticias")
        print("=====================================================")
        sistema.menu_principal()
    except KeyboardInterrupt:
        print("\n\nAplicación interrumpida por el usuario.")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        print("Ocurrió un error inesperado. Verifica el log para más detalles.")
    finally:
        print("\nGracias por usar el sistema.")

if __name__ == "__main__":
    main()
