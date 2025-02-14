print('************************ DESEMPAQUETADO DE TUPLA ************************')
#producto = ('p001', 'Camisa', 20.00)
#id,descripcion,precio = producto[0],producto[1],producto[2]
#for element in producto:
#    print(element, end=' , ')
##id,descripcion,precio = producto
#print(producto)
#print(f'ID:{id}')
#print(f'Descripcion:{descripcion}')
#print(f'Precio: ${precio}')
#print('\n')

print('************************ DESEMPAQUETADO DE TUPLA ************************')
print('Lista de tuplas')

productos = [
    ('p001','Camisa  ', 20.00),
    ('p002','Jeans   ', 30.00),
    ('p003','Sudadera', 40.00)
]

precio_total = 0
print('Informacion de los productos:')

for element in productos:
    #print(element)
    id,descripcion,precio = element
    print(f'Id: {id} , Descripción: {descripcion} , Precio: {precio:.2f}')
    precio_total+= precio

print(f'Precio Total = ${precio_total:.2f}')








