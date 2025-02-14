nombreLibro = input(f'Ingrese el nombre del libro --> ')
idLibro = int(input(f'Ingrese el ID del libro --> '))
precioLibro = float(input(f'Ingrese el precio del libro --> '))
envioGratuito = False
envioGratuito = (input('Indique con True o False , si el envio es gratis --> '))

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == False:
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True/False'
    envioGratuito = (input('Indique con True o False , si el envio es gratis --> '))

print(f'''

Título del libro: {nombreLibro}
El id: ({idLibro})
Precio: ${precioLibro}
Envio gratuito: {envioGratuito}

''')
1








