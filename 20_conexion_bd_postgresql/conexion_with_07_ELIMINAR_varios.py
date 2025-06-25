# https://www.psycopg.org/docs/usage.html#with-statement
import psycopg2
conexion = psycopg2.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input(f'Ingrese el ID a eliminar:  (separados por comas) ')
            entrada1 = tuple(entrada.split(','))
            valores = (entrada1,)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados en la tabla test_db: ({registros_eliminados})')

except Exception as e:
    print(f'Ocurrio un error: {e}')  # Es útil mostrar el error real
finally:
    conexion.close()

