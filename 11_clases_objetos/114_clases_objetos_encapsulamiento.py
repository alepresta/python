print('****************** CLASES Y OBJETOS ******************* ')
print('****************    Encapsulamiento   ******************* ')

'''
El encapsulamiento nos permite ocultar la información que almacena un objeto
ESTADO DE UN OBJETO

self._nombre  PROTEGIDO
self.__nombre PRIVADO

METODOS ---> GET y SET

'''

class Coche:

    def __init__(self,marca,modelo,color):
        self.marca = marca     # atributo público
        self._modelo = modelo  # atributo protegido
        self.__color = color   # atributo privado

    def conducir(self):
        print(f'''
        Marca: {self.marca}
        Modelo: {(self._modelo)}
        Color: {(self.__color)}''')

if __name__ == '__main__':
    coche1 = Coche(marca='Ford',modelo='Focus',color='Negro')
    coche2 = Coche('Toyota', 'Yaris','Azul')
    coche2.conducir()
    coche1.conducir()

