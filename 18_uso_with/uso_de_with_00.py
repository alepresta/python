from ManejoArchivos import ManejoArchivos

print('******** uso de with *************')
#with open('prueba.txt') as archivo:
#    print(archivo.read())


with ManejoArchivos('prueba.txt') as archivo:
    archivoQ = open('prueba.txt', 'r')
    archivo = open('prueba.txt', 'a')
    archivo.write(f'Hola gato\n')
    archivo.write('Wild\n')
    archivo.write(archivoQ.read())
