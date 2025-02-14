def convertidorFahrenheitToCelsius(fahrenheit):
    celsius = (float(fahrenheit) -32 ) * 5 / 9
    return celsius

def convertidorCelsiusToFahrenheit(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

tipo = int(input('''
Ingrese 0 para fahrenheit a celsius
Ingrese 1 para celsius a fahrenheit
---> aquí: ->
'''))

if tipo == 0:
    fahrenheit = float(input('Ingrese el valor en grados Fahrenheit: '))
    celsius = convertidorFahrenheitToCelsius(fahrenheit)
    print(f'{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius')
elif tipo == 1:
    celsius = float(input('Ingrese el valor en grados Celsius: '))
    fahrenheit = convertidorCelsiusToFahrenheit(celsius)
    print(f'{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit')
else:
    print('El tipo es incorrecto')

