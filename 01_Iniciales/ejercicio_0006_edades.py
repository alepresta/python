edad = int(input(f'Ingresa tu edad aquí ->'))
mensaje = None

if 0 <= edad < 10:
    mensaje = 'La influencia es increíble'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
else:
    mensaje = 'Etapa de vida incorrecta'


print(f'({edad}) {mensaje}')