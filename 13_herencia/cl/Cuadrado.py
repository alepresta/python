from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # Inicializa FiguraGeometrica (ancho = alto = lado)
        FiguraGeometrica.__init__(self, lado, lado)
        # Inicializa Color
        Color.__init__(self, color)
        self.lado = lado  # Opcional, ya que ancho y alto están en FiguraGeometrica
        self.color = color


    def __str__(self):
        #return f"Cuadrado: Lado={self.lado}, Color={self.color}, Área={self.ancho * self.alto}"
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    @property
    def cuadrado(self,lado):
        return self.lado

    @cuadrado.setter
    def cuadrado(self,lado):
        self.lado = lado


    def calcular_area(self):
        return self.lado * self.lado


