from mi_clase_documentacion import Micla
#help(Micla)
#print(Micla.__doc__)
#print(Micla.__init__.__doc__)

#help(str.capitalize)

mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()



print(f'''
mensaje1: {mensaje1}, {id(mensaje1)}
mensaje2: {mensaje2}, {id(mensaje2)}
''')
mensaje1 += 'adios'
print(f'''
mensaje1: {mensaje1}, {id(mensaje1)}
''')