titulo = '****      Sistema de Administración de Cuentas     ****'
seleccion = '''
Menu:
    1- Crear cuenta
    2- Eliminar cuenta
    3- Salir   
    
    ----->>> escribir aqui: 
'''
eliminando_cuenta = 'Eliminando tu cuenta ...\n'
creando_cuenta = 'Creando tu cuenta....\n'
salir_cuenta = 'Saliendo de tu cuenta...\n'
print('*** Sistema de Administracion de cuentas  ***')
'''
respuesta = 0
while respuesta != 3:
    respuesta = int(input(f'opcion de {seleccion}'))
    if respuesta == 1:
        print(creando_cuenta)
    elif respuesta == 2:
        print(eliminando_cuenta)
    elif respuesta == 3:
        print(salir_cuenta)
    else:
        print("respuesta equivocada")
'''

salir = False
while not salir:
    respuesta = int(input(f'opcion de {seleccion}'))
    if respuesta == 1:
        print(creando_cuenta)
    elif respuesta == 2:
        print(eliminando_cuenta)
    elif respuesta == 3:
        salir = True
        print(salir_cuenta)
    else:
        print("¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿respuesta equivocada¡¡¡¡¡¡¡¡¡¡¡¡¡ \n")
else:
    print('FIN \n')