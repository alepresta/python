from os import MFD_ALLOW_SEALING

print('*************** CAJERO AUTOMATICO ***************')

'''
Opciones:
Depositar 
retirar
Consultar el saldo

valor_inicial 1000
'''
valor_iniciial = 1000
salir = False
while not salir :
    pantalla = float(input('''
     1- Depositar, 2- Retirar, 3- Consultar Saldo,  4- Salir
    ------>  
    '''))
    if pantalla == 1:
        print(f'Su saldo es de: ${valor_iniciial:.2f} pesos')
        deposito = float(input('¿Cuanto dinero quiere depositar? -->  '))
        valor_iniciial = valor_iniciial + deposito
        print(f'Su nuevo saldo es de: ${valor_iniciial:.2f} pesos')
        print('')

    elif pantalla == 2:
        print(f'Su saldo es de: ${valor_iniciial:.2f} pesos')
        retiro = float(input('¿Cuanto dinero quiere retirar? -->  '))
        print(f'Su nuevo saldo es de: ${valor_iniciial:.2f} pesos')
        print('')
        if retiro >= valor_iniciial:
            print(f'No podes retirar ${retiro} porque tenes ${valor_iniciial}')
            retiro = float(input('¿Cuanto dinero quiere retirar? -->  '))
            valor_iniciial = valor_iniciial - retiro
            print(f'Su nuevo saldo es de: ${valor_iniciial:.2f} pesos')
            print('')
        else:
            valor_iniciial = valor_iniciial - retiro
    elif pantalla == 3:
        print(f'Su saldo es de: ${valor_iniciial:.2f} pesos')
    elif pantalla == 4:
        salir = True
        print('Saliendo del sistema ....')
    else:
        print('la opción elegida es inválida ...')
else:
    print('FIN')







