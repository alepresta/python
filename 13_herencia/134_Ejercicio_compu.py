print('#################### Ejercicio Compu ####################')
print('#################### Ejercicio parte 1 ####################')
class DispositivoEntrada:
    def __init__(self,tipo,marca):
        self.tipo = tipo
        self.marca = marca

    def __str__(self):
        return f'''Tipo:{self.tipo}, Marca:{self.marca}'''

raton1 =   DispositivoEntrada('  Ratón', 'Samsung')
raton2 =   DispositivoEntrada('  Ratón', 'Genius')
raton3 =   DispositivoEntrada('  Ratón', 'Genius')
teclado1 = DispositivoEntrada('Teclado', 'Samsung')
teclado2 = DispositivoEntrada('Teclado', 'Genius')
teclado3 = DispositivoEntrada('Teclado', 'LG')
print (f'  raton1 = [{raton1}]')
print (f'  raton2 = [{raton2}]')
print (f'  raton3 = [{raton3}]')
print (f'teclado1 = [{teclado1}]')
print (f'teclado2 = [{teclado2}]')
print (f'teclado3 = [{teclado3}]')

print('#################### Ejercicio parte 2 ####################')

class Monitor:
    cantidad_monitores = 0

    def __init__(self,id_monitor,marca,tamanio):
        self.id_monitor = id_monitor
        self.marca = marca
        self.tamanio = tamanio
        Monitor.cantidad_monitores += 1

    def __str__(self):
        #return f'id={self.id_monitor}, marca={self.marca}, tamaño={self.tamanio} dirección:{super.__str__(self)}'
        return f'id={self.id_monitor}, marca={self.marca}, tamaño={self.tamanio}'

    @classmethod
    def contador_monitor(cls):
        return cls.cantidad_monitores


monitor1 = Monitor('01','Samsung','20 pulgadas')
monitor2 = Monitor('02','Termaltek','50 pulgadas')
monitor3 = Monitor('03','LG','50 pulgadas')
print(f'Cantidad de monitores = Monitor.contador_monitor()')
print(f'''
Monitor1={monitor1}, 
Monitor2={monitor2}''')

print('#################### Ejercicio parte 3 ####################')

class Computadora:
    contador_compu = 0
    def __init__(self,id, nombre, monitor, teclado, raton):
        self.id = id
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
        Computadora.contador_compu += 1

    def __str__(self):
        return f'''        Id:{self.id}
        Nombre:{self.nombre}
        Monitor:{self.monitor}
        Teclado:{self.teclado}
        Ratón:{self.raton}'''

    @classmethod
    def contador_computadoras(cls):
        return cls.contador_compu


compu1 = Computadora('01','Dell',monitor1,teclado1,raton1)
compu2 = Computadora('02', 'Mac', monitor2, teclado2, raton2)
compu3 = Computadora('03', 'LG', monitor3, teclado3, raton3)
print(f'Cantidad de computadoras: {Computadora.contador_computadoras()}')
print(compu1)
print(compu2)

print('#################### Ejercicio parte 4 ####################')

class Orden:
    def __init__(self,id,computadora_id):
        self.id = id
        self.computadora_id = computadora_id

    def __str__(self):
        return f'''Orden de compra N°: {self.id}:
{self.computadora_id}'''

    def agregar_computadora(self,id,nombre,monitor,teclado,raton):
        compu = Computadora(id, nombre, monitor, teclado, raton)
        return compu


orden1 = Orden('01',compu1)
orden3 = Orden('03',compu3)
print(orden1)
print(orden3)









