print('************************ Comprensión de listas ************************')
# listas a partir de: ----> (listas, tuplas, set, diccionarios)

'''# LISTA:
numeros = [1,2,3,4,5,6]
pares = []
print(f'Lista de números: ')
print(numeros, end=' ')
print('')
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(f'Los pares son: ')
print(pares, end=" ")

print('')
# NUEVA LISTA:
numeros = [1,2,3,4,5]
for num in numeros:
    cuadrado = num ** 2
    print(f'{num}²={cuadrado}', end='  ')
'''

numeros = [1, 2, 3, 4, 5, 6]
print(f'Lista de números: {numeros})')
print(f'Los pares son: {[x for x in numeros if x % 2 != 0]}')

print( [num ** 2 for num in numeros] )

var = "presta"
print( True if var == 'presta' else False )

nombres = ['Ana', 'Jerónimo', 'Carlos']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)






