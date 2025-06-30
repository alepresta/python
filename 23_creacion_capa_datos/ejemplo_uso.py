from generar_personas_ficticias import GeneradorPersonasCompleto
from persona_dao import PersonaDAO
from persona import Persona  # <-- Esta importación faltaba
import config_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    generador = GeneradorPersonasCompleto(db_config=config_db.DATABASE)

    # Ejemplo 1: Generar 5 personas automáticamente y guardar en DB
    logger.info("Generando 5 personas automáticamente...")
    personas_auto = generador.generar_personas(5, insertar_db=True)
    for p in personas_auto:
        logger.info(f"Generada: {p}")

    # Ejemplo 2: Generar persona manualmente
    logger.info("\nGenerando persona manualmente...")
    persona_manual = generador.generar_persona()
    persona_manual.nombre = "Juan"
    persona_manual.apellido = "Pérez"
    persona_manual.email = "juan.perez@example.com"
    persona_insertada = PersonaDAO.insertar(persona_manual)
    logger.info(f"Persona manual insertada: {persona_insertada}")

    # Ejemplo 3: Generar persona con algunos datos manuales y otros automáticos
    logger.info("\nGenerando persona semi-automática...")
    persona_semi = generador.generar_persona()
    persona_semi.nombre = "María"
    persona_semi.apellido = "González"
    persona_insertada = PersonaDAO.insertar(persona_semi)
    logger.info(f"Persona semi-automática: {persona_insertada}")

    # Ejemplo 4: Borrar un registro por ID
    logger.info("\nProbando eliminación...")
    if personas_auto:
        id_a_eliminar = personas_auto[0].id_persona
        logger.info(f"Eliminando persona con ID: {id_a_eliminar}")
        persona_a_eliminar = Persona(id_persona=id_a_eliminar)
        if PersonaDAO.eliminar(persona_a_eliminar):
            logger.info("Persona eliminada exitosamente")
        else:
            logger.error("No se pudo eliminar la persona")

    # Ejemplo 5: Listar todas las personas
    logger.info("\nListado completo de personas:")
    personas = PersonaDAO.seleccionar()
    for p in personas:
        logger.info(p)


if __name__ == "__main__":
    main()