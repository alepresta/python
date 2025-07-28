import mysql.connector
from conexion_db1 import DATABASE

personas_db = mysql.connector.connect(**DATABASE)
cursor = personas_db.cursor()
sentencia_00 = ('INSERT INTO personas (nombre, apellido, edad) '
                'VALUES (%s, %s, %s)')

datos_valores = ('Victor', 'Ramos', 46)
parametros_01 = ('Juan', 'Pérez', 30)


cursor.execute(sentencia_00,datos_valores )
cursor.execute(sentencia_00,parametros_01)

personas_db.commit()

cursor.close()
personas_db.close()