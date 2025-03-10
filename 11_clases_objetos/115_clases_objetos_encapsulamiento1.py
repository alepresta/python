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

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color

if __name__ == '__main__':
    coche1 = Coche(marca='Ford',modelo='Focus',color='Negro')
    coche2 = Coche('Toyota', 'Yaris','Azul')
    # coche2.conducir()
    coche1.conducir()
    print(f'Marca: {coche1.marca}')
    coche1.marca ='Fiat'
    print(f'Cambio de marca a Fiat:')
    coche1.conducir()
    setattr(coche1,'nuevo_atributo','valor_nuevo_atributo')
    print(coche1.nuevo_atributo)
    print(coche1.__dict__)
    print(coche2.__dict__)