import psycopg2 as bd
conexion = bd.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido,email) VALUES(%s,%s,%s)'
            valores = ('Alex','Rojas','arojas@email.com')
            cursor.execute(sentencia,valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores= ('Juan', 'Perez', 'jperez@email.com',1)
            cursor.execute(sentencia,valores)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
print('Termina la transacción')
