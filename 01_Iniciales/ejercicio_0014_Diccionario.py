# Diccionario | KEY | VALUE |
diccionario = {
    'IDE': 'Integrated Development Eviroment',
    'OOP': 'Object Oriented Programing',
    'DBMS': 'Database Management System'
}

print(diccionario)

#largo
print(len(diccionario))
print(diccionario['IDE'])
print(diccionario.get('OOP'))
diccionario['IDE'] = '1ntegrated 3evelopment 3viroment'
print(diccionario['IDE'])
print(f'---------------------------------------------------------------')
for termino , valor in diccionario.items():
    print(f'Termino:{termino}, Valor:{valor}')

print(f'---------------------------------------------------------------')
for termino in diccionario.keys():
    print(termino)
print(f'---------------------------------------------------------------')
for valores in diccionario.values():
    print(valores)
print(f'---------------------------------------------------------------')

print( 'IDE' in diccionario)
print(f'---------------------------------------------------------------')
diccionario['PK'] = 'Primary Key'
print(diccionario)


print(f'-------------------REMOVER--------------------------------------------')
diccionario.pop('DBMS')
print(diccionario)
diccionario.clear()
del diccionario


