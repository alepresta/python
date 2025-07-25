import mysql.connector

personas_db = mysql.connector.connect(
    host='85.31.224.145',
    user='apresta',
    password='miamigodardo1pa',
    database='personas_db'
)
# password = 'Seguridad1@!',
mi_cursor = personas_db.cursor()
mi_cursor.execute('SELECT * FROM personas')
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)