def desplegarNombres(nombres):
    for nombre in nombres:
        print(f'nombre: {nombre} ')

nombres = [ 'Juan' , 'Pedro' , 'Lautaro', 'Carla' , 'Guillermo' , 'Maria' , 'Ana', 'Laura' ]

desplegarNombres(nombres)
desplegarNombres('Juan')
# ERROR desplegarNombres(10)
desplegarNombres((8,9))
desplegarNombres([11,88])