from os.path import split

help(str.join)

print(f' Tupla '.center(20,'*'))
tupla_str = ('Hola', 'Mundo', 'Unviversidad', 'Python')
print(tupla_str)
mensaje = '- -'.join(tupla_str)
print(mensaje)
print(f' Lista '.center(20,'*'))
lista_cursos = [ 'java', 'Python', 'Angular', 'Stpring']
mensaje1 = ', '.join(lista_cursos)
print(mensaje1)
print(f' String '.center(20,'*'))
un_string1 = 'Hola mundo'
mensaje3 = '.'.join(un_string1)
print(mensaje3)
print(f' Diccionario '.center(20,'*'))
diccionario = {'nombre':'Juan','apellido': 'Perez', 'edad': '18'}
mensaje4 = ' '.join(diccionario)
print(f'{mensaje4}, tipo:{type(diccionario)}')



print(f' SPLIT '.center(20,'*'))
mensaje5 = un_string1.split()
print(f'{mensaje5}, tipo:{type(mensaje5)}')

cursos_separados_por_coma = 'java,Python,Angular,Stpring,Excel'
mensaje6 = cursos_separados_por_coma.split()
print(f'{mensaje6}, tipo:{type(mensaje5)}')