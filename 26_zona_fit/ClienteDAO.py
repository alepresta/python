from cliente import Cliente
from conexion import Conexion

class ClienteDAO():

    def listar():
        conetado = Conexion.conectar()
        SELECCIONAR = 'SELECT id, nombre, apellido, membresia FROM personas ORDER BY id'
        cursor = conetado.cursor()
        cursor.execute(SELECCIONAR)
        print(''.center(30, '*'))
        datos_clientes = cursor.fetchall()
        for datos in datos_clientes:
            print(datos)

    @staticmethod
    def insertar(nombre, apellido, membresia):
        conetado = Conexion.conectar()
        INSERTAR = 'INSERT INTO personas(nombre, apellido, membresia) VALUES(%s, %s, %s)'
        cursor = conetado.cursor()
        cursor.execute(INSERTAR,(nombre,apellido,membresia))
        conetado.commit()
        print(f'Usted agrego: {nombre}, {apellido}, {membresia}')


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
        ELIMINAR = 'DELETE FROM personas WHERE id=%s'
        coenex = Conexion.conectar()
        cursor = coenex.cursor()
        cliente_a_eliminar = Cliente
        cliente_a_eliminar.id
        cursor.execute(ELIMINAR,(id,))
        coenex.commit()
