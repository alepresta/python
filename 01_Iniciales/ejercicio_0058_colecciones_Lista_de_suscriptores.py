print('************************ Lista de suscriptores ************************')
suscriptores = set()
agregar = False
salir = False
while not salir:
    quiere_agregar = str(input('Quiere agregar suscriptores: (SI/NO): ->  '))
    quiere_agregar =  quiere_agregar.strip().lower()
    if quiere_agregar == 'no':
        print(f'Lista: {suscriptores}')
        numero_suscriptores = int(input('Ingrese el numero a Eliminar: --->  '))
        for _ in range(numero_suscriptores):
            suscriptor_a_eliminar = input(f'Ingrese el suscriptor a eliminar: --> ')
            suscriptores.remove(suscriptor_a_eliminar)
    else:
        print(f'Lista: {suscriptores}')
        numero_suscriptores = int(input('Numero a agregar: --->  '))
        for _ in range(numero_suscriptores):
            nuevo_suscriptor = input('Ingrese mail suscriptor: --->  ')
            if nuevo_suscriptor in suscriptores:
                print(f'El nuevo suscriptor: ({nuevo_suscriptor}) ya esta en la lista ')
            else:
                suscriptores.add(nuevo_suscriptor)
                print(f'El nuevo suscriptor: ({nuevo_suscriptor}) se agregó a la lista ')
    quiere_salir = input(f'Usted quiere salir: (SI/NO) -->  ')
    quiere_salir = quiere_salir.strip().lower()
    if quiere_salir == 'no':
        salir = False
    else:
        salir = True


cantidad_total_de_suscriptores = len(suscriptores)
print(f'\nLista de suscriptores: cantidad({cantidad_total_de_suscriptores})')
for suscriptor in suscriptores:
    print(f'- ({suscriptor})')
