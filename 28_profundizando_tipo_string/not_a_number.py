print(' Not a Number '.center(25,"-"))
# NaN no es un numero nan Nan NAN
# Es un tipo de dato numérico para un valor indefinido
a = float('NaN')

import math




print(a)
print(f'¿Es NaN (no a number)?: {math.isnan(a)}')


import locale

# Configurar el locale en español (puede variar según el sistema)
try:
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # Linux/Mac
    # locale.setlocale(locale.LC_ALL, 'es_ES')     # Windows
except locale.Error:
    print("El locale 'es_ES' no está disponible en tu sistema.")

help(str.capitalize)