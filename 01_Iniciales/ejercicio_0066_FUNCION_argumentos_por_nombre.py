print('********** FUNCIÓN ARGUMENTO POR NOMBRE **********')


def imprimir_persona(nombre,apellido='',edad=0):
    print(f'Hola {nombre} {apellido} tu edad es: {edad} años ')


imprimir_persona('Ale','Presta',50)
imprimir_persona( apellido='Prestico',edad=32 ,nombre='Wildburd')
imprimir_persona(apellido='Fuentes',nombre='Carlos')