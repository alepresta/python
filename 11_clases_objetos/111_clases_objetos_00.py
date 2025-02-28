print('****************** CLASES Y OBJETOS ******************* ')
print('****************    CONSTRUCTORES   ******************* ')
'''
Un constructor es un método para crear un objeto
Ademas para inicializar atributos de un nuevo objeto
'''
#------------------------------------------------------------------------
class Pirulo:
        def __init__(self,parametro1,parametro2):
            self.parametro1 = parametro1
            self.parametro2 = parametro2
        def mostrar_pirulo(self):
            print(self.parametro1,self.parametro2)
#------------------------------------------------------------------------
class Gato:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_gato(self):
        print(self.nombre,self.edad)
#------------------------------------------------------------------------
class Persona:
    def inicializar_persona(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def mostrar_persona(self):
        print(self.nombre, self.apellido)
#------------------------------------------------------------------------
# CREACIÓN DE OBJETOS
if __name__ == '__main__':
    persona1 = Persona()
    persona1.inicializar_persona('Pepito', 'Acosta')
    persona1.mostrar_persona()
    print(f'Dirección memoria persona1 {id(persona1)}')
    print(f'Dirección memoria hexadecimal persona1 {hex(id(persona1))}')
    print(f'{persona1}')
    print('')
    persona2 = Persona()
    persona2.inicializar_persona('Juan', 'Gómez')
    persona2.mostrar_persona()
    print(f'Dirección memoria persona2 {id(persona2)}')
    print('')
# ------------------------------------------------------------------------
    pirulo = Pirulo('piru','lo')
    pirulo.mostrar_pirulo()
    print(f'Dirección memoria pirulo {id(pirulo)}')
    print('')
#------------------------------------------------------------------------
    gato = Gato('Miau','Miau')
    gato.mostrar_gato()
    print(f'Dirección memoria gato {id(gato)}')
    print('')
