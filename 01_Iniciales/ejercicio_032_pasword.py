print('*** Sistema de Autenticación ***')
usuario_valido = 'admin'
password_valido = '123'

user = input('¿Cuál es tu nombre?   --->   ')
psw = input('¿Cuál es tu password? --->   ')

user = user.strip()
psw = psw.strip()

es_correcto = user == usuario_valido and psw == password_valido

print((f'Los datos {user} son: {es_correcto}'))



