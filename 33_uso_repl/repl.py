class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        nombre = self.nombre
        apellido = self.apellido
        #id = hex(id(self)).upper()
        return f'Nombre: {nombre} Apellido: {apellido} ID: {hex(id(self)).upper()}'.ljust(80,' ')

persona = Person('Juan', 'Fuentes')


print(' '.center(50,'-'))
print(f'Ocho formas de crear un bool false'.center(50,'*'))
print(' '.center(50,'-'))
persona1 = None
persona2 = ''
persona3 = []
persona4 = ()
persona5 = {}
persona6 = 0
persona7 = 0.00
persona8 = False

if bool(persona1):
    print(f'({persona1}) Se considera verdadera , tipo: {type(persona1)}'.ljust(50,' '))
else:
    print(f'({persona1}) Se considera falsa , tipo: {type(persona1)}'.ljust(50,' '))

if bool(persona2):
    print(f'({persona2}) Se considera verdadera , tipo: {type(persona2)}'.ljust(50,' '))
else:
    print(f'({persona2}) Se considera falsa , tipo: {type(persona2)}'.ljust(50,' '))

if bool(persona3):
    print(f'({persona3}) Se considera verdadera , tipo: {type(persona3)}'.ljust(50,' '))
else:
    print(f'({persona3}) Se considera falsa , tipo: {type(persona3)}'.ljust(50,' '))

if bool(persona4):
    print(f'({persona4}) Se considera verdadera , tipo: {type(persona4)}'.ljust(50,' '))
else:
    print(f'({persona4}) Se considera falsa , tipo: {type(persona4)}'.ljust(50,' '))

if bool(persona5):
    print(f'({persona5}) Se considera verdadera , tipo: {type(persona5)}'.ljust(50,' '))
else:
    print(f'({persona5}) Se considera falsa , tipo: {type(persona5)}'.ljust(50,' '))

if bool(persona6):
    print(f'({persona6}) Se considera verdadera , tipo: {type(persona6)}'.ljust(50,' '))
else:
    print(f'({persona6}) Se considera falsa , tipo: {type(persona6)}'.ljust(50,' '))

if bool(persona7):
    print(f'({persona7}) Se considera verdadera , tipo: {type(persona7)}'.ljust(50,' '))
else:
    print(f'({persona7}) Se considera falsa , tipo: {type(persona7)}'.ljust(50,' '))

if bool(persona8):
    print(f'({persona8}) Se considera verdadera , tipo: {type(persona8)}'.ljust(50,' '))
else:
    print(f'({persona8}) Se considera falsa , tipo: {type(persona8)}'.ljust(50,' '))


















print('FIN')