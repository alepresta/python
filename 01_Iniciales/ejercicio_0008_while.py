# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del while')
#
# min = 1
# cont = 5
# while cont >= 1:
#     print(cont)
#     cont -= 1
# else:
#     print('Fin While x')
# -------------------------------------------------
# cadena = 'Hola'
#
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin del FOR')
contPar = 0
contInpar = 0
cont = 0
min = 0
max = 6
for i in range(max):
    if i % 2 != 0:
        contInpar += 1
        continue
    contPar += 1
    print(f'Valor: {i}')

print(f'Pares:({contPar}), Impares:({contInpar})')
print(f'Minimo:({min}), Máximo:({max})')
