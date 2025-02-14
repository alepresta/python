print('********* CALCULADORA *********')


salir = False
while not salir :
    operando_1 = float(input('Ingrese operando 1 ---->  '))
    operando_2 = float(input('Ingrese operando 1 ---->  '))
    opciones = '''1. Sumar | 2. Restar | 3. Multiplicación |4. División | 5. Salir
    Escriba aquí (1|2|3|4|5):--------->   '''
    print(f'¿Que quiere hacer con los números: ({operando_1:.2f}) y ({operando_2:.2f})?')
    opcion_seleccionada = int(input(f'{opciones}'))
    if opcion_seleccionada == 1:
        print(f'{operando_1} + {operando_2} = {operando_1 + operando_2}')
    elif opcion_seleccionada == 2:
        print(f'{operando_1} - {operando_2} = {operando_1 - operando_2}')
    elif opcion_seleccionada == 3:
        print(f'{operando_1} x {operando_2} = {operando_1 * operando_2}')
    elif opcion_seleccionada == 4:
        print(f'{operando_1} / {operando_2} = {operando_1 / operando_2}')
    elif opcion_seleccionada == 5:
        print('Saliendo del sistema ........')
        salir = True
    else:
        print('¡El número ingresado es incorrecto!')
print('FIN')

