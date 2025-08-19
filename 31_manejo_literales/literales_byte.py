from boltons.iterutils import split

print(f' Literales tipo byte '.center(40,'*'))

caracteres_en_bytes = b'Hola Mundo'

print(caracteres_en_bytes[0])

print(chr(caracteres_en_bytes[0]))


lista_caracteres_en_bytes = caracteres_en_bytes.split()

print(f'mensaje sin split: {caracteres_en_bytes}')
print(f'mensaje con split: {lista_caracteres_en_bytes}')

print('')


print(f' convertir cadena a byte '.center(40,'*'))
string = 'Programación con Python'

string_bytes = string.encode('utf-8')
string_bytes_02 = string_bytes.decode('utf-8')

print(f'String original: {string}')
print(f'String encode bytes: {string_bytes}')
print(f'String Dencode bytes: {string_bytes_02}')

