mes = int(input(f'''
Ingrese mes: 
Enero (1), Febrero (2), Marzo (3), Abril (4), 
Mayo (5), Junio (6), Julio (7), Agosto(8), 
Septiembre (9), Octubre (10), Noviembre (11), Diciembre (12)
  aquí ->
'''))

estacion = None

if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:
    estacion = 'Mes incorrecto'

print(f'La estación del mes ({mes}) es: ({estacion})')
