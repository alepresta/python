print(' Unpaking '.center(50,'*'))


lista_de_numeros = [1,2,3]
#print(lista_de_numeros)
#print(*lista_de_numeros)
#print(*lista_de_numeros, sep='-')
#print(*lista_de_numeros,sep='\n')

diccionario_de_numeros = (1,2,3)
#print(diccionario_de_numeros)
#print(*diccionario_de_numeros)
#print(*diccionario_de_numeros, sep='-')

def sumar(a,b,c):
    print(f'{a}+{b}+{c}={a+b+c}')



#sumar(1,2,3)

sumar(*diccionario_de_numeros)














