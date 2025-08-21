print(f' Alinear Cadenas '.center(50,'*'))
print(f' Centrar un string '.center(50 , ' '))

ics = '\U0001f102'
titulo = ' Sitio Web de GlobalMentoring.com '
print(f'Longitud string {len(titulo)}')

print(titulo.center(len(titulo)+30,ics)) #Centrado
print(titulo.ljust(len(titulo)+30,ics)) # Izquierda
print(titulo.rjust(len(titulo)+30,ics)) # Derecha
print(titulo.replace(' ','_')) # reemplazo
print(titulo.strip(' S').center(len(titulo)+30,ics)) # QUitar primero y último
print('')



nuevo_titulo =  ' *** Sitio Web de GlobalMentoring.com *** '
print(nuevo_titulo) #Centrado
print(nuevo_titulo.rstrip('* '))  # Quita las * de la derecha
print(nuevo_titulo.lstrip(' *'))  # Quita las * de la izquierda

nuevo_titulo1 = nuevo_titulo.strip() # quitar caracteres en blanco
nuevo_titulo1 = nuevo_titulo1.strip('*')
nuevo_titulo1 = nuevo_titulo1.strip()

nuevo_titulo2 = nuevo_titulo.strip().strip('*').strip()

print(nuevo_titulo1)
print(nuevo_titulo2)







