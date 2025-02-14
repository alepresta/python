print('*** Valor dentro de rango ***')
valor_minimo = 0
valor_maximo = 5
numero_usuario = int(input(f'Ingresa un número entre {valor_minimo} y {valor_maximo}: '))

# resultado = numero_usuario >= valor_minimo  and  numero_usuario <= valor_maximo
resultado = valor_minimo <= numero_usuario <= valor_maximo

print(f'Está dentro del rango: {resultado}')