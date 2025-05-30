class Animal:
    def comer(self):
        print("comer mucho")

    def dormir(self):
        print("dormir mucho")

class Perro(Animal):
    def hacer_sonido(self):
        print("Ladrar")

    def dormir(self):
        print("duerme un perro 15 horas")



if __name__ == '__main__':
    print('************* Ejemplo de herencia en python *************')

    animal = Animal()
    perro = Perro()
    animal.comer()
    animal.dormir()
    perro.hacer_sonido()
    perro.dormir()