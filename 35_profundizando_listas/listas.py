print(' Listas '.center(50,'*'))
nombres_01 = ['juan', 'Karla', 'Pedro']
nombres_02 = 'Laura Juan Maria gonzalo Ernesto'.split()

nombres_03 = nombres_01 + nombres_02

print(nombres_03)
#for nombre in nombres_03:
#    print(nombre)


numeros = [10,40,15,4,20,90,4]
print(numeros)
numeros.reverse()
print(numeros)
numeros.sort(reverse=False)
print(numeros)
numeros.sort(reverse=True)
print(numeros)

print(' Valor minimo y maximo '.center(50,'*'))
print(min(numeros))
print(max(numeros))
print(' Copiar una lista '.center(50,'*'))
numeros_copiados = numeros.copy()
print(numeros_copiados)

