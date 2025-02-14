print('************************ Diccionario ************************')
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
'''print(f'    Nombre: {persona["nombre"]}')
print(f'    Edad: {persona.get("edad")}')
print(f'    Ciudad: {persona["ciudad"]}')'''


persona['edad'] = 35
persona['profesion'] = 'ingeniero'
#del persona['ciudad']
#persona.pop('profesion')

print(persona)
print('')
for llave, valor in persona.items():
    print(f'LLave: {llave},  Valor: {valor}')
print('')
for value in persona.values():
    print(f'LLave: {value}')
for key in persona.keys():
    print(f'Key: {key}')






