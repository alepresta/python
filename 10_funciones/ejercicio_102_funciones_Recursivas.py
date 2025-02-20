print('************* FUNCIONES Recursivas *************')

def funcion_recursiva(numero):
    if numero == 1:
        print(numero, end=' ')
    else:
        print(numero, end=' ')
        funcion_recursiva(numero-1)
        #print(numero, end=' ')

funcion_recursiva(5)