print('************************** Manejo de archivos ***************************')

archivo = open('/home/prestaa/Workspace/python/17_manejo_archivos/prueba.txt', 'r', encoding='utf8')

#print(archivo.read(5))
#print(archivo.read(3))
#print(archivo.read())
#-------------------------------
#print(archivo.readline())
#-------------------------------
#for linea in archivo:
#    print(linea)
#-------------------------------
#print(archivo.readlines())
#-------------------------------
#print(archivo.readlines()[2])
#-------------------------------
#copiar un archivo haciendo copia del original

archivo2 = open('/home/prestaa/Workspace/python/17_manejo_archivos/copia.txt', 'w')
archivo2.write(archivo.read())

archivo2.close()
archivo.close()

