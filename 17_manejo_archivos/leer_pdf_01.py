print('************************** Leer pdf ***************************')

archivo = open('prueba.txt','r')



archivo2 = open('prueba.txt', 'a')
archivo2.write(f'Hola gato'+  archivo.read())

archivo2.close()
