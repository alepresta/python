
print('*** Sentencias IF ***')
edad = int(input('Ingresa tu edad: ---->>    '))
if edad >= 18 :
    print(f'Como tienes {edad} años se te considera mayor de edad')
elif 13 <= edad < 18:
    print(f'Como tienes {edad} años se te considera adolecente')
else:
    print(f'Como tienes {edad} años se te considera niñito')