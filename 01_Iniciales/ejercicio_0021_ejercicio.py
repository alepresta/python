# def imprimeDescendente(numeros):
#     if numeros <= 0:
#         print(f'({numeros}): No imprime nada')
#     else:
#         valor = numeros
#         while 1 <= valor <= numeros:
#             print(f'{valor}')
#             valor = valor - 1
#


def imprimeDescendente(numero):
    if numero > 1:
        print(numero)
        imprimeDescendente(numero -1)
    elif numero < 0:
        print(f'({numero}) valor incorrecto')
    elif  numero == 1 or numero == 0:
        print(f'{numero}')




imprimeDescendente(1)