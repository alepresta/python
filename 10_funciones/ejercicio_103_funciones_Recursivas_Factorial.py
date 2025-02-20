print('************* FUNCIONES RECURSIVA FACTORIAL *************')

def funcion_factorial(numero):
    if numero == 0 or numero ==1 :
        print(f'Resultado factorial pacial {numero} es: (1)')
        return 1
    else:
        factorial_parcial = numero * funcion_factorial(numero-1)
        print(f'Resultado factorial pacial {numero} es: ({factorial_parcial})')
        return factorial_parcial





funcion_factorial(5)

