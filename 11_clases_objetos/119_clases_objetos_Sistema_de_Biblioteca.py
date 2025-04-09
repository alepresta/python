print('******************   CLASES Y OBJETOS   ******************* ')
print('****************   SISTEMA DE BIBLIOTECA  ***************** ')


class Libro:
    libros = []

    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        Libro.libros.append(self)

    def agregar_libro(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        print(f'[Agregado ok]{"\t"} {self._titulo.ljust(35)}')

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero

    @classmethod
    def buscar_libro_por_autor(cls, autor):
        autor = autor.strip().lower()
        libros_encontrados = []
        for libro in cls.libros:
            if libro.autor.lower() == autor:
                libros_encontrados.append(libro)

        if libros_encontrados:
            print("Libros encontrados:")
            for libro in libros_encontrados:
                print(libro.titulo.ljust(35), ' | ', libro.autor.ljust(25), ' | ', libro.genero.ljust(20))
        else:
            print(f"No se encontraron libros del autor: {autor}")

    @classmethod
    def buscar_libro_por_genero(cls, genero):
        genero = genero.strip().lower()
        libros_encontrados = []
        for libro in cls.libros:
            if libro.genero.lower() == genero:
                libros_encontrados.append(libro)

        if libros_encontrados:
            print("Libros encontrados:")
            for libro in libros_encontrados:
                print(libro.titulo.ljust(35), ' | ', libro.autor.ljust(25), ' | ', libro.genero.ljust(20))
        else:
            print(f"No se encontraron libros del género: {genero}")

    @classmethod
    def mostrar_todos_los_libros(cls):
        print("\nTodos los libros en la biblioteca:")
        print("Título".ljust(35), " | ", "Autor".ljust(25), " | ", "Género".ljust(20))
        print("-" * 85)
        for libro in cls.libros:
            print(libro.titulo.ljust(35), ' | ', libro.autor.ljust(25), ' | ', libro.genero.ljust(20))

    def mostrar_un_libro(self):
        print("\nInformación del libro:")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Género:", self.genero)


if __name__ == '__main__':
    libro1 = Libro(titulo='', autor='', genero='')
    libro2 = Libro(titulo='', autor='', genero='')
    libro3 = Libro(titulo='', autor='', genero='')
    libro4 = Libro(titulo='', autor='', genero='')
    libro5 = Libro(titulo='', autor='', genero='')
    libro6 = Libro(titulo='', autor='', genero='')
    libro7 = Libro(titulo='', autor='', genero='')
    libro8 = Libro(titulo='', autor='', genero='')
    libro9 = Libro(titulo='', autor='', genero='')
    libro10 = Libro(titulo='', autor='', genero='')

    libro1.agregar_libro(titulo='Cien años de soledad', autor='Gabriel García Márquez', genero='Realismo mágico')
    libro2.agregar_libro(titulo='1984', autor='George Orwell', genero='Ciencia ficción distópica')
    libro3.agregar_libro(titulo='Orgullo y prejuicio', autor='Jane Austen', genero='Romance clásico')
    libro4.agregar_libro(titulo='El señor de los anillos', autor='J.R.R. Tolkien', genero='Fantasía épica')
    libro5.agregar_libro(titulo='Crónica de una muerte anunciada', autor='Gabriel García Márquez',
                         genero='Novela dramática')
    libro6.agregar_libro(titulo='Don Quijote de la Mancha', autor='Miguel de Cervantes', genero='Novela clásica')
    libro7.agregar_libro(titulo='Harry Potter y la piedra filosofal', autor='J.K. Rowling', genero='Fantasía juvenil')
    libro8.agregar_libro(titulo='La sombra del viento', autor='Carlos Ruiz Zafón', genero='Misterio, drama')
    libro9.agregar_libro(titulo='Los juegos del hambre', autor='Suzanne Collins', genero='Ciencia ficción distópica')
    libro10.agregar_libro(titulo='El principito', autor='Antoine de Saint-Exupéry',
                          genero='Literatura infantil y filosófica')

    print('---------------buscar_libro_por_autor---------------Gabriel García Márquez')
    Libro.buscar_libro_por_autor('Gabriel García Márquez')

    print('---------------buscar_libro_por_genero---------------Ciencia ficción distópica')
    Libro.buscar_libro_por_genero('Ciencia ficción distópica')

    print('---------------mostrar_todos_los_libros---------------')
    Libro.mostrar_todos_los_libros()

    print('---------------mostrar_un_libro(---------------Los juegos del hambre')
    libro9.mostrar_un_libro()