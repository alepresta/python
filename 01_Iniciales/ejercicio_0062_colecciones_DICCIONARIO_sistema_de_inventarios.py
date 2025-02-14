print('************************ Sistema de Inventarios ************************')

cantidad_productos_a_agregar_al_inventario = int(input(f'Ingresa la cantidad de productos que quieres agregar al inventario: --> '))
lista_almacen = []

for i in range(cantidad_productos_a_agregar_al_inventario):
    nombre_producto = input(f'Ingresa el nombre del producto({i+1}): -->  ')
    precio_producto = float(input(f'Ingresa el precio({i+1}): --> '))
    cantidad_disponible = int(input(f'Ingresa la cantidad disponible({i+1}): -->  '))
    producto = {'id': i+1 , 'nombre': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_disponible}
    lista_almacen.append(producto)



print(f'Lista total:')
for lista in lista_almacen:
    print(lista)


id_buscar = int(input(f'Ingresa el ID a buscar: --> '))
if id_buscar > len(lista_almacen):
    print(f'ID Equivocado ERROR ')
else:
    print(f'ID:({id_buscar})')
    print(lista_almacen[id_buscar])










