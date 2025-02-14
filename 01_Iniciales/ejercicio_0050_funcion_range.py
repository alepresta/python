print('********* Repetición de un mensaje *********')

mensaje = input('Proporciona un mensaje a repetir --->')
cuantas_repeticiones = int(input('¿Cuantas repeticiones?: -->'))

for _ in range(cuantas_repeticiones):
    print(f'{mensaje}')