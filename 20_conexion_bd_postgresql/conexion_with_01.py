# https://www.psycopg.org/docs/usage.html#with-statement
import psycopg2
conexion = psycopg2.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            param = (1,2)
            cursor.execute(sentencia, (param,))
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error ')
finally:
    conexion.close()

