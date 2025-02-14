print('************************ PROMEDIO CALIFICACIONES ************************')
total_calificaciones = 0
calificaciones = []
numero_calificaciones_a_evaluar = int(input('Ingrese el número de calificaciones a evaluar: -->  '))

for i in range(numero_calificaciones_a_evaluar):
    nota = int(input(f'Ingrese calificación ({i}): ->>  '))
    calificaciones.append(nota)
    total_calificaciones = total_calificaciones + nota

promedio = total_calificaciones / numero_calificaciones_a_evaluar
suma_de_todas_las_calificaciones = sum(calificaciones)


print('\n')
for calificacion in calificaciones:
    print(calificacion , end='+')
print(f' = {total_calificaciones} , El promedio es: {promedio:.2f}')

print(f'sum(calificaciones)= {suma_de_todas_las_calificaciones}')












