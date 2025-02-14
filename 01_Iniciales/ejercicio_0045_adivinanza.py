print('************ ADIVINAR NÚMERO SECRETO ************')
import random
salir = False
numero_aleatorio = random.randint(1,50)
#print(f'numero_aleatorio: {numero_aleatorio}')
print('Elegir un numero de 1 al 50')

intentos_maximos = 5
contador = 1
while not salir:
    numero_propuesto_usuario = int(input(f'Intento: ({contador}) número aquí: --->   '))

    if contador >= intentos_maximos:
        salir = True
        print(f'¡PERDISTE! Te costo el max de intentos que es: ({contador}) JAJAJ el número era: {numero_aleatorio}')
    elif numero_propuesto_usuario == numero_aleatorio:
        print(f'¡GANASTE!  Te costo ({contador}) intentos el numero era: ({numero_aleatorio})')
        salir = True
    elif numero_propuesto_usuario < numero_aleatorio:
        print(f'El numero aleatorio es mayor a: {numero_propuesto_usuario}')
    elif numero_propuesto_usuario > numero_aleatorio:
        print(f'El numero aleatorio es menor a: {numero_propuesto_usuario}')
    contador += 1






