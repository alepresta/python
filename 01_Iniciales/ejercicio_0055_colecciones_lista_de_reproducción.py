print('************************ LISTA  REPRODUCCCIÓN ************************')

playlist = []
#playlist.append('Hotel California - Eagles')
#playlist.append('Staying Alive - Bee Gees')
#playlist.append('Dream on - Aerosmith')

#ordenar alfabéticamente SORT

#playlist.sort()
#playlist.sort(reverse=True)
#print(playlist)


for canciones in playlist:
    print(canciones , end=' ')
print('\n')


numero_canciones = int(input('¿Cuantas canciones queres agregar? --->  '))



for i in range(numero_canciones):
    canciones_a_agregar = input(f'Ingrese la canción ({i}) : --->  ')
    playlist.append(canciones_a_agregar)














print('\n')
print('Así queda la playlist')
for canciones in playlist:
    print(canciones , end=", ")
print('\n')





