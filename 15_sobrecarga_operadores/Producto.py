print(" Sobrecarga de Operadores ".center(50, "="))

class Producto:
    contador_de_productos = 0

    def __init__(self,nombre, precio):
        Producto.contador_de_productos += 1
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'{self.nombre} = ${self.precio} '

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre