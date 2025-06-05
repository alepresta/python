from CatalogoPeliculas import CatalogoPeliculas
from Pelicula import Pelicula

def mostrar_menu():
    print('\n   Catalogo de peliculas   '.center(40, '-'))
    print('(1) Agregar película'.center(40, ' '))
    print('(2) Listar películas'.center(40, ' '))
    print('(3) Eliminar catálogo'.center(40, ' '))
    print('(4) Salir'.center(40, ' '))
    print(''.center(40, '-'))

def main():
    url_del_catalogo = '/home/prestaa/Workspace/python/18_zcatalogo_peliculas/catalogo_peliculas/catalogo_peliculas.txt'
    catalogo = CatalogoPeliculas(url_del_catalogo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
            print(f"Película '{nombre_pelicula}' agregada correctamente!")

        elif opcion == '2':
            print("\nListado de películas:")
            catalogo.listar_peliculas()

        elif opcion == '3':
            confirmacion = input("¿Está seguro de eliminar el catálogo? (s/n): ")
            if confirmacion.lower() == 's':
                catalogo.eliminar_catalogo()
                print("Catálogo eliminado correctamente")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()