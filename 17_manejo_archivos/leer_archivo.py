print('************************** Clase Manejo de archivos ***************************')

class ManejoArchivos:
    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Óbtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_exepcio,valor_excepcion, traza_error):
        print('cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()

with ManejoArchivos('libro.pdf') as archivo:
    print(archivo.read())