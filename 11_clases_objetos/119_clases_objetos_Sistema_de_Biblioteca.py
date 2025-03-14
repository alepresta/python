print('******************   CLASES Y OBJETOS   ******************* ')
print('****************   SISTEMA DE BIBLIOTECA  ***************** ')


class Libro:
    def __init__(self,titulo,autor,genero):
        self.titulo = titulo
        self.autor  = autor
        self.genero = genero













if __name__ == '__main__':
    libro1 = Libro(titulo='Cien años de soledad', autor='Gabriel García Márquez', genero='Realismo mágico')
    libro2 = Libro(titulo='1984', autor='George Orwell', genero='Ciencia ficción distópica')
    libro3 = Libro(titulo='Orgullo y prejuicio', autor='Jane Austen', genero='Romance clásico')
    libro4 = Libro(titulo='El señor de los anillos', autor='J.R.R. Tolkien', genero='Fantasía épica')
    libro5 = Libro(titulo='Crónica de una muerte anunciada', autor='Gabriel García Márquez', genero='Novela dramática')
    libro6 = Libro(titulo='Don Quijote de la Mancha', autor='Miguel de Cervantes', genero='Novela clásica')
    libro7 = Libro(titulo='Harry Potter y la piedra filosofal', autor='J.K. Rowling', genero='Fantasía juvenil')
    libro8 = Libro(titulo='La sombra del viento', autor='Carlos Ruiz Zafón', genero='Misterio, drama')
    libro9 = Libro(titulo='Los juegos del hambre', autor='Suzanne Collins', genero='Ciencia ficción distópica')
    libro10 = Libro(titulo='El principito', autor='Antoine de Saint-Exupéry', genero='Literatura infantil y filosófica')


    print(f'| {libro1.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro2.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro3.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro4.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro5.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro6.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro7.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro8.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro9.titulo} | {libro1.autor} | {libro1.genero} |')
    print(f'| {libro10.titulo} | {libro1.autor} | {libro1.genero} |')