print('&&&&&&&&&&&&&&&&&&  BREAK &  CONTINUE  &&&&&&&&&&&&&&&&&&')

#Ejemplo con break
for numero in range(1,10+1):
    if numero % 2 == 0:
        print(f'{numero}')
        break

print('\n')

for numero in range(1,10+1):
    if numero % 2 == 1:
        print(f'{numero}')
        continue
    print(f'c{numero}')










