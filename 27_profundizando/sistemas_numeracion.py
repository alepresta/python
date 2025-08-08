#profundizando en sistmas de numeración

# Decimal (0,1,2,3,4,5,6,7,8,9) Base = 10
a = 10

# Binario (0,1) Base = 2
a = 0b1010

# Octal (0,1,2,3,4,5,6,7,8) Base = 8
a = 0o12

# Hexadecimal (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F) Base = 16
a = 0xA

#Resultado
print(f'a:{a}')

# Convertir un tipo entero, incluyendo base
print(f'----')
# Base = 10
a = int('23', 10) # base decimal

a = int('10111',2) # Base = 2 Binario

a = int('27',8) # Base = 8 Octal

a = int('17',16) # Base = 16 Hexadecimal

print(f'a:{a}')

print(f'--- Profundizando tipo Float ---')
#Profundizando tipo Float
f  = 3
print(f'a:{f:.2f}')

f = float('10')
print(f'f:{f}')

print(f'-- exp --')
ex = 3e-5
print(f'ex:{ex:.10f}')

print(type(ex))


print(f'--- INFINITO ---')

import math

#infinito_positivo = 'inf'
infinito_positivo = float('inf') # infinito positivo
infinito_positivo = float('-inf')# infinito negativo
print(f'Infinito positivo: {infinito_positivo}')

print(f'Es un valor infinito?: {math.isinf(infinito_positivo)}')
print(f'Es un valor infinito (¿negativo /Positivo?): {infinito_positivo}')

















