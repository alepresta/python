"""
condicion = 10

if condicion == True:
    print('Condición verdadera')
elif condicion == False:
    print('Condición falsa')
else:
    print('Condición no reconocida')
"""


numeroTexto = ''
numero = int(input(f'ingrese un numero 1-3 -->  '))

if numero == 1:
    numeroTexto = 'UNO'
elif numero == 2:
   numeroTexto = 'DOS'
elif numero == 3:
    numeroTexto = 'TRES'
else:
    numeroTexto = 'Fuera de rango 1-3'

print(f"El numero que seleccionó es: ({numero}) , {numeroTexto}")