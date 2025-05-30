# Calse Object
#__init__() inicializar
#__str__() mandar a imprimir el estado de un objeto
#__eq__() poder comparar si 2 metodos son iguales

print(f'******************** Clase object ********************')


class Persona:
    def __init__(self, nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self): # sobreeescribir el metodo __str__
        return f'''   Persona:
                Nombre: {self.nombre}
                Apellido: {self.apellido}
                Dirección de memoria: {super.__str__(self)}'''

persona1 = Persona('Ana', 'Martinez')
print(persona1)
