print('************* FUNCIONES ARGUMENTOS VARIABLES *************')

def superheroe_powers(superheroe, nombre, *args):
    print(f'''
    Super héroe: {superheroe} - Nombre: {nombre}
    args: {args}
    ''')
print('-----')

def superheroe_kwargs(superheroe, nombre, *args, **kwargs):
    print(f'''
    Super héroe: {superheroe} - Nombre: {nombre}
    argumentos: {args}
    kwargs: 
    ''')
    for llave,valor in kwargs.items():
        print(f'{llave}:{valor}')

superheroe = 'Spiderman'
nombre = 'Peter Parker'
poderes = 'Instinto arácnido', 'Telearaña'
kwargs = 'nombre="Karla", edad= 38 , pais="Mexico"'

superheroe_powers(superheroe,nombre,poderes)
print('-----')
#superheroe_kwargs(superheroe,nombre,poderes,nombre='Karla', edad=38 , pais='Mexico')

def imp(**kwargs):
    print(f'Valores recibidos:')
    for llave,valor in kwargs.items():
        print(f'{llave}:{valor}')


imp(nombre="Karla", edad=38 , pais="Mexico")