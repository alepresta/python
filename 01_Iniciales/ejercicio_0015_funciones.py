#FUNCIONES

def miFuncionE(nombre, apellido):
    print(f'Saludos {nombre} {apellido} desde mi Func')

# miFuncionE('ale', 'presta')
# miFuncionE('Carla', 'Lara')
# miFuncionE('Juan', 'Perez')

def sumar(a,b):
    return a + b
#
# resultado = sumar(4,3)
# print(resultado)


def listarNombres(*nombres):
    tupla = nombres
    return tupla
sTupla = listarNombres('Ale', 'Gaby', 'Pedro', 'Roberto', 'Ana', 'Laura', 'Juana', 'Melisa' , 'Romina', 'Luisa', 'Andrea')
sTupla = listarNombres('Lucas', 'Lucio')

for nombre in sTupla:
    print(nombre)
























