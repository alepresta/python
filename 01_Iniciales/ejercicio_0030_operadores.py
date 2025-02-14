#operadores aritméticos
a = 10
b = 3

# Opciones para obtener un resultado flotante:
suma1 = float(a) + b
suma2 = a + float(b)
suma = a + b

print(f"Suma 1: {suma1:.2f}")
print(f"Suma 2: {suma2:.2f}")
print(f"Suma 2: {suma:.2f}")

# % resto
modulo = a % b
divi = a//b
div = a/b
print(f'division 10 / 3 = {divi} (division común//)')
print(f'division 10 // 3 = {divi} (division entera//)')
print(f'resto 10 % 3 = {modulo}')

exponente = a**b
print(f'Exponente 10 ** 3 esto es = {exponente} o (10 °3ra)')

nombre, apellido = input('Nombre , apellido: --> ').split(',')
print(f'Nombre: {nombre} y el apellido: {apellido}')

print('-------------------------------------------')
a,b = 10,15
print(f'a = 10 , b = 15')
print('-------------------------------------------')
a+=b
print(f'a +=b --> ({a})')
a+=b
print(f'a +=b --> ({a})')
a+=b
print(f'a +=b --> ({a})')
a+=b
print(f'a +=b --> ({a})')
print('-------------------------------------------')
a = 10
a *=b
print(f'a *=b --> ({a})')
a *=b
print(f'a *=b --> ({a})')
a *=b
print(f'a *=b --> ({a})')
a *=b
print(f'a *=b --> ({a})')
print('-------------------------------------------')
