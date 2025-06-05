from ManejoMisDatos import ManejoMisDatos


class CatalogoPeliculas:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f"{pelicula}\n")

    def listar_peliculas(self):
        try:
            with ManejoMisDatos(self.ruta_archivo) as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print("El catálogo no existe o está vacío")

    def eliminar_catalogo(self):
        import os
        try:
            os.remove(self.ruta_archivo)
            return True
        except FileNotFoundError:
            return False