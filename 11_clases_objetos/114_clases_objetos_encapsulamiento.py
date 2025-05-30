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
        self._marca = marca     # atributo público
        self._modelo = modelo  # atributo protegido
        self._color = color   # atributo privado

    def conducir(self):
        print(f'''
        Marca: {self._marca}
        Modelo: {(self._modelo)}
        Color: {(self._color)}''')

    def get_marca(self):
        return self._marca
    def set_marca(self,marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo
    def set_model(self,modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color
    def set_color(self,color):
        self._color = color

if __name__ == '__main__':
    coche1 = Coche(marca='Ford',modelo='Focus',color='Negro')
    coche2 = Coche('Toyota', 'Yaris','Azul')
    # coche2.conducir()
    coche1.conducir()
    print(f'Marca: {coche1.get_marca()}')
    coche1.set_marca('Fiat')
    print(f'Cambio de marca a Fiat:')
    coche1.conducir()

