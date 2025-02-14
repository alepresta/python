#recetas
print('******************* RECETAS COCINA ******************* ')

nombre_receta = input(str('Inrgrese nombre del plato: -->   '))
ingredientes = input(str('Ingrese los ingredientes: -->   '))
tiempo = int(input('Ingrese el tiempo de preparación: (en minutos) -->   '))
dificultad = str(input('Ingrese Fácil , Mediano, Dificil: -->   '))
print('----------------------------------------------------------')

print(f'Receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación {tiempo} minutos')
print(f'Nivel de dificultad: {dificultad}')
