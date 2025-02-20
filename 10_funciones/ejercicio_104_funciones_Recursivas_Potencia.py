print('************* FUNCIONES RECURSIVA POTENCIA *************')

# 2 ** 3 = 2*2*2= 8
# 6**2 = 6*6 = 36

def potencia(numero,potencia):
    resultado = numero ** potencia
    print(f'Resultado de ({numero}) ** {potencia} = {resultado}')
    return resultado

potencia(4,5)
potencia(4,0)
potencia(4,10)

def potencia_recursiva(numero, potencia):
    if potencia == 0:
        return 1
    else:
        return numero * potencia_recursiva(numero,potencia-1)

numero = 4
potenci = 5
print(f'Resultado RECURSIVO ({numero}) ** {potenci} = {potencia_recursiva(numero,potenci)}')
numero = 4
potenci = 0
print(f'Resultado RECURSIVO ({numero}) ** {potenci} = {potencia_recursiva(numero,potenci)}')
numero = 4
potenci = 10
print(f'Resultado RECURSIVO ({numero}) ** {potenci} = {potencia_recursiva(numero,potenci)}')
