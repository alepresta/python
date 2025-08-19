print(f' CADENAS '.center(20,'*'))

nombre = 'Juan'
edad = 28
mensaje_con_formato= 'Mi nombre es: %s y tengo %d años'%(nombre,edad)

print(f'{mensaje_con_formato}')

print('')

persona = ('Karla', 'Gomez', 5000.00)
mensaje_con_formato1 = f'Mi nombre es %s %s tengo $%s pesos en el banco'%persona

print(mensaje_con_formato1)




persona2 = ( 'Juan', 'Carlos', 'Argentino', ' Caballero', 'Distribuidor', 5000.001 , 'Dolares')
formater = '%s,%s,%s,%s,%s,u$s %.3f,%s  '%persona2

print(formater)

numeros = '%d'
flotantes = '%.2f'
string = '%s'


nombre1 = ('Juan')
edad1 = 30
sueldo1 = 5000.01

mensaje_con_formato2 = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre1,edad1,sueldo1)
print(mensaje_con_formato2)

mensaje_con_formato3 = 'Edad {1} Sueldo {2:.2f} Nombre {0}'.format(nombre1,edad1,sueldo1)
print(mensaje_con_formato3)

mensaje_con_formato4 = 'Nombre:{n} Edad:{e} Sueldo:u$s{s:.2f}'.format(n=nombre,e=edad,s=sueldo1)

print(mensaje_con_formato4)


print(f' Diccionario '.center(20,'*'))
diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 585.05}

mensaje_con_formato5 = 'Nombre{persona[nombre]} Edad:{persona[edad]} Sueldo:u$s{persona[sueldo]} '.format(persona= diccionario)

print(mensaje_con_formato5)
print('')
print('')
print(f' Listas '.center(20,'*'))
resultado = 5*'hola'
resultado = 5* ('hola',5,500.01,'Amigo')

resultado = 5*(5*resultado[0] , 5*resultado[3])


print(resultado)















