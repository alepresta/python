print('************* FUNCIONES ARGUMENTOS EJERCICIO PAR O IMPAR *************')

def es_par(*num):
    pares = []
    impares = []
    for valor in num:
        if valor % 2 == 0:
            #print(f'({valor}):par')
            pares.append(valor)
        else:
            #print(f'({valor}):impar')
            impares.append(valor)
    print(f'Todo: {num}')
    print(f'Pares: {pares}')
    print(f'Impares: {impares}')


es_par(7,3,4,5,6,7,8,9,22,33,45,67)
