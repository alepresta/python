print('************* FUNCIONES celsius fahrenheit *************')

def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 +32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32 ) * 5/9

salir = False
while not salir:
    print('')
    print('1- celsius a fahrenheit')
    print('2- fahrenheit a celsius')
    print('3- salir')
    funcione= int(input(f'Desea convertir (1/2/3): -> '))
    if funcione == 1:
        celsius = float(input('Ingrese celsius: -> '))
        fa = celsius_a_fahrenheit(celsius)
        print(f'celsius:({celsius:.2f}) a fahrenheit =  ({fa:.2f})')
    elif funcione == 2:
        fa = float(input('Ingrese fahrenheit: -> '))
        celsius = fahrenheit_a_celsius(fa)
        print(f'fahrenheit:({fa:.2f}) a celsius =  ({celsius:.2f})')
    elif funcione == 3:
        salir = True
    else:
        print(f'Opción inválida ')




