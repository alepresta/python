from cliente import Cliente
from conexion import Conexion


class ClienteDAO():

    def listar():
        try:
            conetado = Conexion.conectar()
            SELECCIONAR = 'SELECT id, nombre, apellido, membresia FROM personas ORDER BY id'
            cursor = conetado.cursor()
            cursor.execute(SELECCIONAR)
            print(''.center(30, '*'))
            datos_clientes = cursor.fetchall()
            clientes = []
            for datos in datos_clientes:
                cliente = Cliente(datos[1], datos[2], datos[3], datos[0])
                clientes.append(cliente)
            for cliente in clientes:
                print(
                    f"ID: {str(cliente.id).center(4)} | "
                    f"{str(cliente.nombre).ljust(10)} | "
                    f"{str(cliente.apellido).ljust(10)} | "
                    f"Membresía: {str(cliente.membresia).ljust(10)}"
                )
            return clientes

        except Exception as e:
            print(f'Ocurrio un error: {e}')
        finally:
            if conetado is not None:
                cursor.close()
                Conexion.liberar_conexion(conetado)

    @staticmethod
    def insertar(nombre, apellido, membresia):
        try:
            conetado = Conexion.conectar()
            INSERTAR = 'INSERT INTO personas(nombre, apellido, membresia) VALUES(%s, %s, %s)'
            cursor = conetado.cursor()
            cursor.execute(INSERTAR,(nombre,apellido,membresia))
            conetado.commit()
            print(
                f" | Usted Agrego a:  | "
                f"{str(nombre)} "
                f"{str(apellido).ljust(10)} | "
                f"Membresía: {str(membresia).ljust(10)} | "
            )
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un errror al insertar: {e}')
        finally:
            if conetado is not None:
                cursor.close()
                Conexion.liberar_conexion(conetado)


    @staticmethod
    def actualizar(nombre, apellido, membresia,id):
        ACTUALIZAR = 'UPDATE personas SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
        conectation = Conexion.conectar()
        cursor = conectation.cursor()
        cursor.execute(ACTUALIZAR,(nombre,apellido, membresia, id))
        conectation.commit()
        print(f'Usted actualizo ID({id}): {nombre}, {apellido}, {membresia}')

    @staticmethod
    def eliminar(id):
        try:
            coenex = Conexion.conectar()
            cursor = coenex.cursor()

            # Primero obtenemos los datos del cliente a eliminar
            OBTENER_CLIENTE = 'SELECT nombre, apellido, membresia FROM personas WHERE id=%s'
            cursor.execute(OBTENER_CLIENTE, (id,))
            cliente_data = cursor.fetchone()

            if cliente_data is None:
                print(f"No se encontró un cliente con ID {id}, por lo tanto NO SE ELIMINO EL ID: ({id})")
                return

            # Ahora ejecutamos la eliminación
            ELIMINAR = 'DELETE FROM personas WHERE id=%s'
            cursor.execute(ELIMINAR, (id,))
            coenex.commit()

            # Mostramos los datos del cliente eliminado
            print(
                f" | Usted Elimino a:  | "
                f"{str(cliente_data[0])} "
                f"{str(cliente_data[1]).ljust(10)} | "
                f"Membresía: {str(cliente_data[2]).ljust(10)} | "
            )
        except Exception as e:
            print((f'Ocurrio un errror: {e}'))
        finally:
            if coenex is not None:
                cursor.close()
                Conexion.liberar_conexion(coenex)

