# https://www.psycopg.org/docs/usage.html#with-statement
import psycopg2
conexion = psycopg2.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO PERSONA(nombre, apellido , email) VALUES(%s, %s, %s)'
            valores = ('Carlos','Lara','clara@email.com')
            valor1 = ('Juan', 'DePablo', 'jdpablo@email.com')
            cursor.execute(sentencia,valores)
            cursor.execute(sentencia,valor1)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: ({registros_insertados})')


except Exception as e:
    print(f'Ocurrio un error: {e}')  # Es útil mostrar el error real
finally:
    conexion.close()

