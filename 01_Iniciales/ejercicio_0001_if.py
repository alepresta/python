"""""

a = int(input('escr n°'))

if a % 2 == 0:
    print(f'El valor: {a} es par')
else:
    print(f'El valor {a} es impar')


edadAdulta = 18
edad = int(input(f'Ingrese su edad aqui -> '))
if edad >= edadAdulta:
    print(f'su edad es: {edad}, por lo tanto es adulto')
else:
    print(f'su edad es {edad}, por lo tanto es Menor')

## Operadores lógicos
# AND OR NOT

a = False
b = False
result = a and b
print(result)


preguntaR = int(input('Ingrese un número aqui ->>>    '))
min = 0
max = 5
if preguntaR >= min and preguntaR <= max:
    print(f'({preguntaR})>={min}  and ({preguntaR})<={max}  | {preguntaR >= min} and {preguntaR <= max} = Es ({preguntaR >= min and preguntaR <= max}) que el n° esta entre {min}-{max}' )
else:
    print(f'({preguntaR})=>{min} and ({preguntaR})<={max}   | {preguntaR >= min} and {preguntaR <= max} = Es ({preguntaR >= min and preguntaR <= max}) que el n° esta entre {min}-{max}' )




"""
Numero1 = int(input(f'Ingrese un número  aqui -->> '))
Numero2 = int(input(f'Ingrese otro número  -->> '))

if Numero1 > Numero2:
    print(f'El número {Numero1} es mayor al número {Numero2}')
else:
    print(f'El número {Numero1} es menor al número {Numero2}')
if Numero1 == Numero2:
    print(f'El número {Numero1} es igual al número {Numero2}')
