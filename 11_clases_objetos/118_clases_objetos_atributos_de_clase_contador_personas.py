print('****************** CLASES Y OBJETOS ******************* ')

class Persona:
    cont = 0  # Contador de instancias

    def __init__(self, nombre, apellido):
        Persona.cont += 1
        self.id = Persona.cont
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id} {self.nombre} {self.apellido}')

    @staticmethod
    def get_cont_estatico():
        return Persona.cont

    @classmethod
    def get_cont_clase(cls):
        return cls.cont


if __name__ == '__main__':
    persona1 = Persona(nombre='Alejandro', apellido='Presta')
    persona2 = Persona(nombre='María', apellido='Gómez')
    persona3 = Persona(nombre='Pablo', apellido='Escobar')
    persona4 = Persona(nombre='Laura', apellido='Fernández')
    persona5 = Persona(nombre='Carlos', apellido='López')
    persona6 = Persona(nombre='Ana', apellido='Martínez')
    persona7 = Persona(nombre='Jorge', apellido='Díaz')
    persona8 = Persona(nombre='Sofía', apellido='Ruiz')


    persona1.mostrar_persona()
    persona2.mostrar_persona()
    persona3.mostrar_persona()
    persona4.mostrar_persona()
    persona5.mostrar_persona()
    persona6.mostrar_persona()
    persona7.mostrar_persona()
    persona7.mostrar_persona()
    persona7.mostrar_persona()
    persona8.mostrar_persona()
    print(f'Persona.cont = {Persona.cont}')
    print(f'Persona.get_cont_estatico() = {Persona.get_cont_estatico()}')
    print(f'Persona.get_cont_clase() = {Persona.get_cont_clase()}')






