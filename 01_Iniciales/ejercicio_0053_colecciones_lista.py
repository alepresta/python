print('************************  COLECCIONES   LISTA  ************************')


mi_lista = [1,2,3,4,5]

print(f'Lista original: {mi_lista}')
largo = len(mi_lista)
print(f'Largo de la lista: {largo}')

print(f'Valor en el indice 4: {mi_lista[4]}')

print(f'Imprime último indice de la lista: {mi_lista[-1]}')

mi_lista[1] = 10
print(f'Modifico el valor 1 de la lista a 10 : {mi_lista}')

mi_lista.append(6)
print(f'Agregar un nuevo elemento al final mi_lista.append(6): {mi_lista}')

mi_lista.insert(2,15)
print(f'Agregar un nuevo elemento mi_lista.insert(2,15): {mi_lista}')


mi_lista.remove(5)
print(f'Remover un elemento mi_lista.remove(5): {mi_lista}')

mi_lista.pop(1)
print(f'Remover un elemento mi_lista.pop(1): {mi_lista}')

del mi_lista[2]
print(f'Remover un elemento del mi_lista[2]: {mi_lista}')

mi_lista = [1,2,3,4,5]
print(mi_lista)
sub_lista = mi_lista[1:3]
print(f'Sublista mi_lista[1:3]:    {sub_lista}')

print('\n')