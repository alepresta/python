# Polimorfismo
class Animal:
    def sonido(self):
        return 'zzzzzzz'

class Perro(Animal):
    def sonido(self):
        return 'guau guau '

class Gato(Animal):
    def sonido(self):
        return 'miau miau'

class Oveja(Animal):
    def sonido(self):
        return 'meeee meee'

class Gallina(Animal):
    def sonido(self):
        return 'ki ki ri ki'

perro = Perro()
print(f'El perro: {perro.sonido()}')
gato = Gato()
print(f'El gato: {gato.sonido()}')
oveja = Oveja()
print(f'El oveja: {oveja.sonido()}')
gallina = Gallina()
print(f'Gallina: {gallina.sonido()}')



