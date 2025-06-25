from conexion import Conexion
from persona import Persona
from persona_dao import PersonaDAO
import random

# Configuración de conexión
config_db = {
    'database': 'test_db',
    'username': 'apresta',
    'password': 'miamigodardo1pa',
    'db_port': '5432',
    'host': '85.31.224.145'
}


def generar_personas_ficticias(cantidad=30):
    """Genera una lista de personas con datos ficticios"""
    nombres_comunes = [
        'Juan', 'María', 'Carlos', 'Ana', 'Luis', 'Laura', 'Pedro', 'Sofía',
        'Diego', 'Isabel', 'Jorge', 'Lucía', 'Fernando', 'Valentina', 'Ricardo',
        'Camila', 'Miguel', 'Daniela', 'José', 'Gabriela', 'Andrés', 'Paula',
        'Francisco', 'Alejandra', 'Antonio', 'Adriana', 'Roberto', 'Natalia',
        'Raúl', 'Verónica'
    ]

    apellidos_comunes = [
        'García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez',
        'Sánchez', 'Pérez', 'Gómez', 'Martín', 'Jiménez', 'Ruiz', 'Hernández',
        'Díaz', 'Moreno', 'Álvarez', 'Muñoz', 'Romero', 'Alonso', 'Gutiérrez',
        'Navarro', 'Torres', 'Domínguez', 'Vázquez', 'Ramos', 'Gil', 'Ramírez',
        'Serrano', 'Blanco', 'Suárez'
    ]

    ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza', 'Málaga',
                'Murcia', 'Palma', 'Bilbao', 'Alicante', 'Córdoba', 'Valladolid']

    dominios = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com']

    personas = []
    for i in range(cantidad):
        nombre = random.choice(nombres_comunes)
        apellido = random.choice(apellidos_comunes)
        email = f"{nombre.lower()}.{apellido.lower()}{random.randint(10, 99)}@{random.choice(dominios)}"
        personas.append(Persona(nombre=nombre, apellido=apellido, email=email))

    return personas


def mostrar_personas():
    """Muestra todas las personas en la base de datos"""
    print("\nListado actual de personas:")
    personas = PersonaDAO.seleccionar()
    if personas:
        for persona in personas:
            print(persona)
    else:
        print("No hay personas registradas")
    print(f"Total registros: {len(personas)}")


def main():
    try:
        # 1. Establecer conexión
        conexion = Conexion.obtener_conexion(config_db)
        print("Conexión establecida correctamente")

        # 2. Insertar 30 personas ficticias
        print("\nInsertando personas ficticias...")
        personas = generar_personas_ficticias(30)

        for persona in personas:
            try:
                PersonaDAO.insertar(persona)
                print(f"Insertado: {persona.nombre} {persona.apellido}")
            except Exception as e:
                print(f"Error insertando {persona.nombre}: {e}")

        # Mostrar estado actual
        mostrar_personas()

        # 3. Operaciones adicionales de ejemplo
        if personas:
            # Actualizar la primera persona
            print("\nActualizando primera persona...")
            todas_personas = PersonaDAO.seleccionar()
            if todas_personas:
                primera_persona = todas_personas[0]
                ciudad = random.choice(['Madrid', 'Barcelona', 'Valencia', 'Sevilla'])
                primera_persona.nombre = f"{primera_persona.nombre} (de {ciudad})"
                if PersonaDAO.actualizar(primera_persona):
                    print(f"Actualizado: {primera_persona.nombre}")

                # Eliminar 5 personas aleatorias
                print("\nEliminando 5 personas aleatorias...")
                for persona in random.sample(todas_personas, min(5, len(todas_personas))):
                    if PersonaDAO.eliminar(persona.id_persona):
                        print(f"Eliminado: {persona.nombre} {persona.apellido}")

                # Mostrar estado final
                mostrar_personas()

    except Exception as e:
        print(f"\nERROR: {e}")
    finally:
        Conexion.cerrar()
        print("\nConexión cerrada")


if __name__ == "__main__":
    main()