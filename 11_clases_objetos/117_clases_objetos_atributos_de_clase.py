# print('****************** CLASES Y OBJETOS ******************* ')

class Persona:

    atributo_clase = 0

    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia



if __name__ == '__main__':
    print('*************  Atributo de clase ******************* ')
    print(f'Atributo clase: {Persona.atributo_clase}')
    Persona.atributo_clase = 1
    print(f'Atributo clase: {Persona.atributo_clase}')
    #print('')
    print('*************  Atributo de instancia ******************* ')
    persona1 = Persona(15)
    print(f'Atributo de clase: {persona1.atributo_clase}')
    print(f'Atributo de instancia: {persona1.atributo_instancia}')

