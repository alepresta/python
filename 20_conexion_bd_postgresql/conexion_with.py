# https://www.psycopg.org/docs/usage.html#with-statement
import psycopg2
conexion = psycopg2.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia = 'SELECT * FROM persona'
            #sentencia = 'SELECT id_persona, nombre FROM persona'
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = int(input('Ingrese el id: -> '))
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchall()
            # registro = cursor.fetchone()  # solo un registro
            print(registros)
            # cursor.close() se cierra solo
except Exception as e:
    print(f'Ocurrio un error ')
finally:
    conexion.close()

