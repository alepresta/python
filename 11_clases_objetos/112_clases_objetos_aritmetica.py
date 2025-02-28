print('****************** CLASES Y OBJETOS ******************* ')
print('****************    ARITMÉTICA   ******************* ')

class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = int(operando1)
        self.operando2 = int(operando2)

    def sumar(self):
        suma = self.operando1 + self.operando2
        print(f'Suma = {self.operando1} + {self.operando2} = {suma}')
        return suma

    def restar(self):
        resta = self.operando1 - self.operando2
        print(f'Resta = {self.operando1} - {self.operando2} = {resta}')
        return resta

    def multiplicar(self):
        multiplicacion = self.operando1 * self.operando2
        print(f'Multiplicacion = {self.operando1} x {self.operando2} = {multiplicacion}')
        return multiplicacion

    def dividir(self):
        division = self.operando1 / self.operando2
        print(f'Division = {self.operando1} / {self.operando2} = {division}')
        return division

#ejercicio
operando1 = 5
operando2 = 7
operando3 = 12
operando4 = 16


valores1 = Aritmetica(operando1,operando2)
valores2 = Aritmetica(operando3,operando4)
Aritmetica.sumar(valores1)
Aritmetica.restar(valores1)
Aritmetica.dividir(valores1)
Aritmetica.multiplicar(valores1)

Aritmetica.sumar(valores2)
Aritmetica.restar(valores2)
Aritmetica.dividir(valores2)
Aritmetica.multiplicar(valores2)

