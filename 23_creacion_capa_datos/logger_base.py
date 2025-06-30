# VER: https://docs.python.org/3/howto/logging.html

# logger_base.py
import logging as log

def configurar_logging():
    """Configuración centralizada del logging para toda la aplicación"""
    log.basicConfig(
        level=log.INFO,  # Puedes cambiar a DEBUG si necesitas más detalle
        format='%(asctime)s: %(levelname)s: [%(filename)s:%(lineno)s] %(message)s',
        datefmt='%I:%M:%S %p',
        handlers=[
            log.FileHandler('capa_datos.log'),
            log.StreamHandler()
        ]
    )

if __name__ == '__main__':
    log.debug('Mensaje nivel debug')
    log.info('Mensaje nivel info')
    log.warning('Mensaje nivel de warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
