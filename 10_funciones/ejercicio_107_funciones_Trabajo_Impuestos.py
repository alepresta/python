print('************* FUNCIONES MAQUINA SNACKS *************')

snaks = [
    {'Id': 1, 'nombre': 'Papas fritas Lay\'s', 'precio': 1.50},
    {'Id': 2, 'nombre': 'Doritos', 'precio': 1.60},
    {'Id': 3, 'nombre': 'Cheetos', 'precio': 1.40},
    {'Id': 4, 'nombre': 'Oreo', 'precio': 2.00},
    {'Id': 5, 'nombre': 'KitKat', 'precio': 1.80},
    {'Id': 6, 'nombre': 'Snickers', 'precio': 1.70},
    {'Id': 7, 'nombre': 'M&M\'s', 'precio': 1.90},
    {'Id': 8, 'nombre': 'Twix', 'precio': 1.75},
    {'Id': 9, 'nombre': 'Galletas Chips Ahoy', 'precio': 2.20},
    {'Id': 10, 'nombre': 'Barra de granola Nature Valley', 'precio': 1.30},
    {'Id': 11, 'nombre': 'Palomitas de maíz Act II', 'precio': 2.50},
    {'Id': 12, 'nombre': 'Pretzels', 'precio': 1.20},
    {'Id': 13, 'nombre': 'Nerds', 'precio': 1.10},
    {'Id': 14, 'nombre': 'Skittles', 'precio': 1.50},
    {'Id': 15, 'nombre': 'Gomitas Haribo', 'precio': 1.40},
    {'Id': 16, 'nombre': 'Chocolates Hershey\'s', 'precio': 1.80},
    {'Id': 17, 'nombre': 'Galletas Ritz', 'precio': 1.60},
    {'Id': 18, 'nombre': 'Barquillos de vainilla', 'precio': 1.90},
    {'Id': 19, 'nombre': 'Pistachos', 'precio': 3.00},
    {'Id': 20, 'nombre': 'Almendras tostadas', 'precio': 2.80},
    {'Id': 21, 'nombre': 'Mix de frutos secos', 'precio': 3.50},
    {'Id': 22, 'nombre': 'Barra de chocolate Lindt', 'precio': 2.50},
    {'Id': 23, 'nombre': 'Galletas Oreo Golden', 'precio': 2.10},
    {'Id': 24, 'nombre': 'Galletas de avena', 'precio': 1.70},
    {'Id': 25, 'nombre': 'Cacahuates japoneses', 'precio': 1.80},
    {'Id': 26, 'nombre': 'Chocolates Ferrero Rocher', 'precio': 3.20},
    {'Id': 27, 'nombre': 'Galletas de mantequilla', 'precio': 1.90},
    {'Id': 28, 'nombre': 'Barra de proteína Clif', 'precio': 2.40},
    {'Id': 29, 'nombre': 'Galletas de arroz', 'precio': 1.50},
    {'Id': 30, 'nombre': 'Chocolates Toblerone', 'precio': 3.50}
]
def mostrar_productos():
    print('\n           ------------------')
    print('           MOSTRAR PRODUCTOS:')
    print('           ------------------')
    for productos in snaks:
        print(f'{productos['Id']:<2} {productos['nombre']:<30} ${productos['precio']:.2f}')

def mostrar_menu():
    print(f'Menú:')
    print(f'   1. Mostrar snaks')
    print(f'   2. Comprar snaks')
    print(f'   3. Mostrar ticket')
    print(f'   4. Salir')


def comprar_snaks():
    carrito = []

    while True:
        print("\n" + "=" * 30)
        print("     🛒 MENÚ DE COMPRAS 🛒")
        print("=" * 30)
        print("1️⃣  Agregar un snack al carrito")
        print("2️⃣  Ver carrito")
        print("3️⃣  Finalizar compra y salir")
        print("=" * 30)

        opcion = input("👉 Elige una opción (1/2/3): ").strip()

        if opcion == "1":
            try:
                id_snack_comprado = int(input("\n🔢 Ingresa el ID del snack que quieres comprar: "))
                encontrado = False

                for producto in snaks:
                    if producto['Id'] == id_snack_comprado:
                        carrito.append(producto)
                        print(f"✅ {producto['nombre']} agregado al carrito por ${producto['precio']}.")
                        encontrado = True
                        break

                if not encontrado:
                    print("❌ Snack no encontrado. Intenta de nuevo.")
            except ValueError:
                print("⚠️  Ingresa un número válido.")

        elif opcion == "2":
            if carrito:
                print("\n" + "=" * 30)
                print("     🛒 CARRITO COMPRAS 🛒")
                print("=" * 30)
                subtotal = sum(item['precio'] for item in carrito)
                for item in carrito:
                    print(f"📌 {item['Id']} - {item['nombre']} - ${item['precio']}")
                print("-" * 30)
                print(f"🧾 Subtotal: ${subtotal}")
                print("=" * 30)
            else:
                print("🛒 El carrito está vacío.")

        elif opcion == "3":
            subtotal = sum(item['precio'] for item in carrito)
            return carrito, subtotal  # Retorna solo el carrito y el subtotal

        else:
            print("❌ Opción inválida. Intenta de nuevo.")




def mostrar_ticket(carrito, total_gastado):
    print('\n')
    print("=" * 30)
    for prod in carrito:
        print(f'{prod['nombre']}: ${prod['precio']}')
    print("=" * 30)
    print(f'Total Gastado: ${total_gastado}')
    print("=" * 30)



#programa principal
if __name__ == '__main__':
    while True:
        print(mostrar_menu())
        opcion = int(input(f'Escoge una opción: -> '))
        if opcion == 1:
            mostrar_productos()
        elif opcion == 2:
            carrito, total_gastado = comprar_snaks()
        elif opcion == 3:
            mostrar_ticket(carrito, total_gastado)
        elif opcion == 4:
            print('Regresa pronto FIN')
            break
        else:
            print(f'La opción: {opcion} es inválida')














# Ejemplo de uso
#mostrar_inventario()
#agregar_producto(1, 'pantuflas', 200, 42)
#mostrar_inventario()
#buscar_producto_por_id(4)









