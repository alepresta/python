print('************************ Diccionario Agenda de contactos ************************')
agenda = {
    'Carlos':  {
        'telefono': '+5491154789653123',
        'email': 'carlos@gmail.com',
        'direccion': 'Calle principal 132'
    },
    'Maria': {
        'telefono': '+5491154789653133',
        'email': 'maria@gmail.com',
        'direccion': 'Calle principal 133'
    },
    'Pedro': {
        'telefono': '+5491154789653134',
        'email': 'pedro@gmail.com',
        'direccion': 'Calle principal 134'
    }
}
print(agenda)
print('')
agenda['Ana'] = {
    'telefono': '+5491154789653135',
    'email': 'ana@gmail.com',
    'direccion': 'Calle principal 135'
}

agenda.pop('Pedro')
del agenda['Pedro']
for nombre in agenda:
    print(f'''Nombre: {nombre}, Telefono: {agenda[nombre]['telefono']}, Email: {agenda[nombre]['email']}, Dirección: {agenda[nombre]['direccion']}''')

print('')
for nombre, detalles in agenda.items():
    print(nombre,detalles)
print('')
#for nombre, valores in agenda.values():
#    print(nombre,valores)
print('')
#for nombre, key in agenda.keys():
#    print(nombre,key)

