print('****************** CLASES Y OBJETOS ******************* ')
print('****************    Encapsulamiento  Operandos ******************* ')

class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self._operando1 = operando1  # Atributo protegido
        self._operando2 = operando2  # Atributo protegido

    # Getters (para obtener valores)
    def get_operando1(self):
        return self._operando1

    def get_operando2(self):
        return self._operando2

    # Setters (para modificar valores)
    def set_operando1(self, nuevo_valor):
        self._operando1 = nuevo_valor

    def set_operando2(self, nuevo_valor):
        self._operando2 = nuevo_valor

    def operaciones(self):
        print(f'Numero1: {self._operando1}, Número2: {self._operando2}')
        print(f'Operaciones disponibles: Sumar, Restar, Multiplicar, Dividir')

    def sumar(self):
        total = self._operando1 + self._operando2
        print(f'({self._operando1} + {self._operando2}) = {total}')
        return total

    def restar(self):
        total = self._operando1 - self._operando2
        print(f'({self._operando1} - {self._operando2}) = {total}')
        return total

    def multiplicar(self):
        total = self._operando1 * self._operando2
        print(f'({self._operando1} × {self._operando2}) = {total}')
        return total

    def dividir(self):
        if self._operando2 == 0:
            print("Error: No se puede dividir por cero.")
            return None
        total = self._operando1 / self._operando2
        print(f'({self._operando1} ÷ {self._operando2}) = {total}')
        return total

if __name__ == '__main__':
    num1 = 12
    num2 = 4
    numeros = Aritmetica(num1, num2)

    # Mostrar operaciones disponibles
    numeros.operaciones()

    # Realizar operaciones
    numeros.sumar()
    numeros.restar()
    numeros.multiplicar()
    numeros.dividir()

    # Obtener valores con getters
    print(f'Valores actuales: {numeros.get_operando1()}, {numeros.get_operando2()}')

    # Modificar valores con setters
    numeros.set_operando1(20)
    numeros.set_operando2(5)

    print(f'Valores modificados: {numeros.get_operando1()}, {numeros.get_operando2()}')

    # Realizar operaciones con los nuevos valores
    numeros.sumar()
    numeros.restar()
    numeros.multiplicar()
    numeros.dividir()

    numeros.set_operando1(11)
    numeros.set_operando2(13)
    numeros.sumar()
    numeros.restar()
    numeros.multiplicar()
    numeros.dividir()