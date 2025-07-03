# logger_base.py
import logging
import sys

def configurar_logging(nombre_logger: str = "capa_datos", nivel=logging.INFO) -> logging.Logger:
    """
    Configura y devuelve un logger con consola y archivo de salida.
    """
    logger = logging.getLogger(nombre_logger)

    if not logger.handlers:  # Evita múltiples configuraciones si ya fue configurado
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: [%(filename)s:%(lineno)d] %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')

        archivo_handler = logging.FileHandler('capa_datos.log')
        archivo_handler.setFormatter(formatter)

        consola_handler = logging.StreamHandler(sys.stdout)
        consola_handler.setFormatter(formatter)

        logger.setLevel(nivel)
        logger.addHandler(archivo_handler)
        logger.addHandler(consola_handler)

    return logger


# Si se ejecuta directamente este archivo, se hace una prueba de logging
if __name__ == '__main__':
    logger = configurar_logging("prueba_logger", logging.DEBUG)
    logger.debug("Mensaje nivel DEBUG")
    logger.info("Mensaje nivel INFO")
    logger.warning("Mensaje nivel WARNING")
    logger.error("Mensaje nivel ERROR")
    logger.critical("Mensaje nivel CRITICAL")
