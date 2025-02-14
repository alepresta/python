print('*** ciclo for ***')
cadena = 'hola mundo'.upper()
for letra in cadena:
    print(letra, end=' ')


print('\n\n***  Recortemos la lista de frutas: *** ')
frutas = ['Melones', 'pomelos', 'peras', 'manzanas']
for tippos_fruta in frutas:
    print(tippos_fruta.upper(), end=' ')


print('\n\n*** Suma acumulativa 1+2+3+4+5 con while ***')
max = 5
count = 1
acumulador = 0

while count <= max:
    numero = count
    acum1 = acumulador
    acumulador += count
    count += 1
    print(f'{numero} + {acum1} = {acumulador}')
print(f'RESULTADO:  = {acumulador}')
print(f"--------------  --------------\n ")


