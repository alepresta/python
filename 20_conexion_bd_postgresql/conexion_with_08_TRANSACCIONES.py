import psycopg2 as bd
conexion = bd.connect(user='apresta',password='miamigodardo1pa',host= '85.31.224.145',port= '5432',database= 'test_db')


try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido,email) VALUES(%s,%s,%s)'
    valores = ('Carlos','Lara','clara@email.com')
    cursor.execute(sentencia,valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores= ('Juan Carlos', 'Juarez', 'jcjuarez@email.com',1)
    cursor.execute(sentencia,valores)

    conexion.commit()
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error: {e}')  # Es útil mostrar el error real
finally:
    conexion.close()

