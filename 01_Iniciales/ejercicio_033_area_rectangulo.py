print('*** Area y perímetro de un rectángulo ***')
base = float(input('Ingrese en centímetros cuanto mide base del rectángulo: --->   '))
altura = float(input('Ingrese la altura en centimetros del rectángulo:      --->   '))

area_rectangulo = base * altura
perimetro_rectangulo = (base + altura) * 2

print(f'El área de un rectángulo de {base}cm x {altura}cm = {area_rectangulo} centímetros cuadrados  ')
print(f'El perímetro de un rectángulo de {base}cm de base y {altura}cm de altura es: {perimetro_rectangulo}cm')