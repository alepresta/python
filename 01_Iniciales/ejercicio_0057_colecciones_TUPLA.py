from logging import logProcesses

print('************************ TUPLA ************************')
# NO SE PUEDE MODIFICAR UNA TUPLA
mi_tuplap = ('elemento_1', 'elmento_2' , 'elemento_3', 'elemento_4')
mi_tupla = (1,2,3,4,5)
print(mi_tupla)

for num in mi_tupla:
    print(num, end=',')
print('\n')

cordenadas =(-34.57548191465449, -58.45110690485308)

print(f'Coordenadas en el eje x: {cordenadas[0]}')
print(f'Coordenadas en el eje y: {cordenadas[1]}')

