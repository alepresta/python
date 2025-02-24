print('************* FUNCIONES SISTEMA INVENTARIOS *************')
# Inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa     ', 'precio': 10.99, 'cantidad': 10},
    {'id': 2, 'nombre': 'Pantalones ', 'precio': 20.99, 'cantidad': 20},
    {'id': 3, 'nombre': 'Zapatos    ', 'precio': 30.99, 'cantidad': 30},
    {'id': 4, 'nombre': 'Camison    ', 'precio': 40.99, 'cantidad': 40},
]

# Función para mostrar el inventario completo
def mostrar_inventario():
    print('------ Inventario del Almacén -------')
    for producto in inventario:
        print(f"{producto['id']:<2} {producto['nombre'].strip():<15} ${producto['precio']:<10.2f} {producto['cantidad']:<10}")

# Función para agregar un nuevo producto al inventario
def agregar_producto(id, producto, precio, cantidad):
    # Verificar si el ID ya existe en el inventario
    for item in inventario:
        if item['id'] == id:
            print(f"Error: Ya existe un producto con el ID {id}.")
            return
    # Si el ID no existe, agregar el nuevo producto
    nuevo_producto = {
        'id': id,
        'nombre': producto.ljust(15),  # Asegura que el nombre tenga 15 caracteres
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(nuevo_producto)
    print(f"Producto '{nuevo_producto}' agregado correctamente.")

def buscar_producto_por_id(id):
    for item in inventario:
        if item['id'] == id:
            print(f'')
            print(f"Producto buscado: id:({item['id']})")
            print(f"{item['id']:<2} {item['nombre'].strip():<15} ${item['precio']:<10.2f} {item['cantidad']:<10}")


# Programa principal
salir = False
while not salir:
        print(f'''\n--- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por id
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))
        # Revisamos las opciones del menu
        if opcion == 1:  # Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2:  # Agregar nuevo producto
            id = int(input(f'Ingrese id: -> '))
            nombre = input(f'Ingrese nombre del producto: -> ')
            precio = float(input(f'Ingrese el precio: -> '))
            cantidad = int(input(f'ingrese la cantidad: -> '))
            agregar_producto(id, nombre,precio,cantidad)
        elif opcion == 3:  # Buscar producto por id
            que = int(input(f'¿Que ID quiere buscar?: -> '))
            buscar_producto_por_id(que)
        elif opcion == 4:  # Salir
            print('Hasta luego!')
            salir = True
        else:
            print('Opción inválida, proporciona una opción válida')





























# Ejemplo de uso
#mostrar_inventario()
#agregar_producto(1, 'pantuflas', 200, 42)
#mostrar_inventario()
#buscar_producto_por_id(4)









