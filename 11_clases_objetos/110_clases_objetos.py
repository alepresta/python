print('****************** CLASES Y OBJETOS ******************* ')

class Persona:
    def inicializar_persona(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(self.nombre, self.apellido)


# CREACIÓN DE OBJETOS
if __name__ == '__main__':
    persona1 = Persona()
    persona1.inicializar_persona('Pepito', 'Acosta')

    persona2 = Persona()
    persona2.inicializar_persona('Juan', 'Gómez')

    persona3 = Persona()
    persona3.inicializar_persona('María', 'Pérez')

    persona4 = Persona()
    persona4.inicializar_persona('Carlos', 'López')

    persona1.mostrar_persona()
    persona2.mostrar_persona()
    persona3.mostrar_persona()
    persona4.mostrar_persona()