#print('  Prueba de Base de Datos  '.center(60,'-'))

import psycopg2

conexion = psycopg2.connect(
    user='apresta',
    password='miamigodardo1pa',
    host= '85.31.224.145',
    port= '5432',
    database= 'test_db'
)

#print(conexion)
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()