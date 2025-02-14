print('=============== Dibujar un triangulo ===============')
'''
Proporciona n° filas
||*
|***
*****
'''
numero_de_filas = int(input('Ingrese el número de filas: ---->'))

for fila in range(1,numero_de_filas+1):
    espacios_en_blanco = ' ' * (numero_de_filas - fila)
    asterisco = '*' * (2 * fila -1)
    print(f'{espacios_en_blanco}{asterisco}')