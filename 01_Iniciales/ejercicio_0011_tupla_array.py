frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[-1])
print(frutas[0:3])

for fruta in frutas:
    print(f'{fruta}',end= ' ')


frutalista = list(frutas)
frutalista[0] = 'Pera'

for fruta in frutalista:
    print(f'{fruta}',end= ' ')

frutalista = tuple(frutalista)