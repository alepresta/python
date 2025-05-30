class Color:
    def __init__(self, color):
        self._color = color

    @property  #atributo get
    def color(self):
        return self._color

    @color.setter   # atributo set
    def color(self,_color):
        self._color = _color

    def __str__(self):
        return f"Color: {self.color}"

