from ClienteDAO import ClienteDAO

def menu():
    print('  Bienvenido a Zona Fit  '.center(30,'*'))
    print(' 1) Listar')
    print(' 2) Agregar')
    print(' 3) Modificar')
    print(' 4) Eliminar')
    print(' 5) Salir')
    print(''.center(30, '*'))
    opcion = int(input('Seleccione una opción 1/5 => '))
    return int(opcion)

def app_zona_fit():
    while True:
        opcion_elegida = menu()
        if opcion_elegida == 1:
            print(f'Usted eligio listar')
            ClienteDAO.listar()
        elif opcion_elegida == 2:
            print(f'Usted elegio agregar')
            print(''.center(30, '*'))
            nombre = input(f'Ingrese el nombre =>  ')
            apellido = input(f'Ingrese el apellido =>  ')
            membresia = input(f'Ingrese el membresia =>  ')
            ClienteDAO.insertar(nombre, apellido, membresia)

        elif opcion_elegida == 3:
            print(f'Usted eligio modificar')
            print(''.center(30, '*'))
            id = int(input(f'Ingrese el ID a modificar => '))
            print(''.center(30, '*'))
            nombre = input(f'Ingrese el nombre =>  ')
            apellido = input(f'Ingrese el apellido =>  ')
            membresia = input(f'Ingrese el membresia =>  ')
            ClienteDAO.actualizar(nombre,apellido,membresia,id)


        elif opcion_elegida == 4:
            print(f'Usted eligio eliminar')
            print(''.center(30, '*'))
            id_a_eliminar = int(input(f'Ingrese el ID a eliminar =>  '))
            ClienteDAO.eliminar(id_a_eliminar)

        elif opcion_elegida == 5:
            print(f'Usted eligio salir')
            print(''.center(30, '*'))
            break
        else:
            print(f'vuelva a elegir una opción válida')
            print(''.center(30, '*'))


