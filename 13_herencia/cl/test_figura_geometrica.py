from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Color import Color
from Rectangulo import Rectangulo

print('Creo un cuadrado')
Figura1Cuadrada = Cuadrado(10,'rojo')
print(Figura1Cuadrada.lado)
print(Figura1Cuadrada.color)
print(f'Area= {Figura1Cuadrada.calcular_area()}')
print('- -')


print('#MRO METHOD Resolution Order')
print(Cuadrado.mro())
print('- -')

print('Creo figura geometrica 3*4')
figura = FiguraGeometrica(3, 4)
print(figura)              # -> FiguraGeometrica [Ancho=3, Alto=4]
print(figura)
print(f'Creo figura geometrica 10 *20')
figura.ancho = 10
figura.alto = 20
print(figura.ancho)        # -> 10
print(figura.alto)         # -> 20
print('- -')

print('Creo un rectangulo 3*4')
rectangulo1 = Rectangulo(3,4, 'rojo')
print(rectangulo1.ancho)
print(rectangulo1.alto)
print(f'Area= {rectangulo1.calcular_area()}')
print('- -')

print(f'Creo un objeto con color rojo y despues verde')
c = Color("Rojo")
print(c)          # -> Color: rojo
c.color = "Verde"
print(c.color)    # -> verde
print('- -')

print('Creo un cuadrado rojo de 10x10')
cuadrado_rojo = Cuadrado(10, "rojo")
print(cuadrado_rojo)
print('- -')