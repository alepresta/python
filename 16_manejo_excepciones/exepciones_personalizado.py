print('*** Manejo de errores personalizado ***')
print('Si A y B son iguales genero una exepción')

class exepcionPersonalizadaIguales(Exception):
    def __int__(self,mensaje):
        self.message = mensaje











resultado = None
a = int(input('Ingrese un número: -->  '))
b = int(input('Ingrese un número: -->  '))
try:
    resultado = a/b
    if a==b:
        raise exepcionPersonalizadaIguales('Numero Identicos')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}, {type(e)}')

except TypeError as e:
    print(f'TypeError - Ocurrió un error {e}, {type(e)}')

except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')


print(f'resultado {resultado}')
print('Continue')