print('*** Tienda de Compras ***')

quiere_comprar = str(input('¿Usted compro algo (si/no)?: ----->   '))
if quiere_comprar.strip().lower() == 'si' :
    importe_comprado = float(input('¿Cual es el importe en pesos que compro?:  --->   '))
    cliente = str(input('¿Usted es cliente (si/no)? --->   '))
    if cliente.strip().lower() == 'si' :
        descuento = importe_comprado * 0.10
        print(f'Usted es cliente y compro ${importe_comprado:.2f}')
        print(f'           Descuento  (-) ${descuento:.2f}')
        print(f'Total con descuento:     ${importe_comprado - descuento}')
    else:
        print(f'Usted no es cliente y compro ${importe_comprado:.2f}')
        print(f'Total a pagar:               ${importe_comprado:.2f}')
else:
    print(f'Usted no quiere comprar nada porque contesto: {quiere_comprar.upper()} . FIN   ')