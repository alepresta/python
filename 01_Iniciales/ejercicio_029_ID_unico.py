
#generar un ID
#valo 4 digitos con rand int

from random import randint
valor_aleatotio = randint(1000,9999)

print(f'valor aleatorio: {valor_aleatotio}')

# id_unico =

# 2 primeras letras del nombre Mayúsculas +
# 2 primeras letras apellido Mayúsculas +
# del año de nacimiento solo 2 ultimas cifras 95 +
# valor_aleatorio 4 cifras

nombre = input(str('Ingresa tu nombre: --> '))
apellido = input(str('Ingresa tu apellido: --> '))
cumpleanos = str(input('Cual es el año de tu nacimiento (YYYY): --> '))


nombre = nombre[:2].upper()
apellido = apellido[:2].upper()
cumpleanos = cumpleanos[-2:]
valor_aleatotio = str(valor_aleatotio)

print(f' Tu ID es: ({nombre+apellido+cumpleanos+valor_aleatotio})')