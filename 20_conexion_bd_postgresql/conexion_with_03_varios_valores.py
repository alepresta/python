# https://www.psycopg.org/docs/usage.html#with-statement
import psycopg2
conexion = psycopg2.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO PERSONA(nombre, apellido , email) VALUES(%s, %s, %s)'
            valores = (
                ('Marcos', 'Cantu', 'mcantu@email.com'),
                ('Angel', 'Quintana', 'aquintana@email.com'),
                ('Maria', 'gonzales', 'mgonzales@email.com')
            )
            cursor.executemany(sentencia,valores)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: ({registros_insertados})')


except Exception as e:
    print(f'Ocurrio un error: {e}')  # Es útil mostrar el error real
finally:
    conexion.close()

