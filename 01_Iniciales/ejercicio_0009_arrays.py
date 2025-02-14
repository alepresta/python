print('----------------------')
nombres = ['Juan', 'Carla', 'Ricardo', 'Pedro', 'Ricardo', 'María']
print(nombres)
# print(nombres[0])
# print(nombres[-1])

# Rango
# print('-----------Rango-----------')
# print(nombres[0:2])
# print(nombres[:3])
# print('----------------------')
# print(nombres[1:])
# print('----------Cambiar Valor------------')
# nombres[1] = 'Carlita'
# print(nombres)
# print('----------Iterar------------')

for nombre in nombres:
    print(f'{nombre}')
else:
    print(f'No existen mas nombres')
    print(f'(len) Longitud array:({len(nombres)})')
print('----------Agregar nuevo elemento------------')
nombres.append('Lorenzo')
nombres.insert(1,'Octavio')
nombres.remove('Octavio')
nombres.pop() #Remueve el último valor
del nombres[0]
nombres.clear
# del nombres
for nombre in nombres:
    print(f'{nombre}')
else:
    print(f'No existen mas nombres')
    print(f'(len) Longitud array:({len(nombres)})')