class ManejoMisDatos:
    def __init__(self,ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def __enter__(self):
        print(f'Obtengo dato'.center(50,'-'))
        self.ruta_archivo = open(self.ruta_archivo, 'r', encoding='utf8')
        return self.ruta_archivo

    def __exit__(self, exc_type, exc_val, exc_tb): #tipo, valor traza
        print(f'libero dato'.center(50,'-'))
        if self.ruta_archivo:
            self.ruta_archivo.close()

