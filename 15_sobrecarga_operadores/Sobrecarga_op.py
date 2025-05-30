print(" Sobrecarga de Operadores ".center(50, "="))


a = 2
b = 3
print(f'{a}+{b}={a+b}')

a = 'hola'
b = 'Mundo'
print(f'{a}+{b}={a+b}')

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre}{other.nombre}'

    def __sub__(self, other):
        return f'{self.edad - other.edad}'


persona1 = Persona('Juan',28)
persona2 = Persona('Carlos',50)
print(persona1+persona2)
print(persona1-persona2)