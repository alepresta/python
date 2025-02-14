print('************************ Diccionario combinado con Lista ************************')

personas = [
    {'nombre': 'Regina',
     'apellido': 'Flores',
     'edad': 21
     },
    {'nombre': 'Alejandro',
     'apellido': 'Reyes',
     'edad': 32
     }
]
print(personas)
print('')

print(personas[0]['apellido'])

for persona in personas:
    print(persona['nombre'],persona['apellido'],persona['edad'])
    #print(personas)