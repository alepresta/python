# https://www.psycopg.org/docs/usage.html#with-statement
import psycopg2
conexion = psycopg2.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s , email = %s WHERE id_persona = %s'
            valores = (
                ('Juan', 'Perez', 'jperez@email.com', 1),
                ('Ivone', 'Gutierrez', 'igutierrez@email.com', 2)
            )
            cursor.executemany(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados en la tabla test_db: ({registros_actualizados})')

except Exception as e:
    print(f'Ocurrio un error: {e}')  # Es útil mostrar el error real
finally:
    conexion.close()

