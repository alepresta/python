print(f' Leer Contenido Online '.center(50, '*'))

from urllib.request import urlopen, Request

# Agregar headers para simular un navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

req = Request('https://pre2-back.argentina.gob.ar/agencia-de-administracion-de-bienes-del-estado-0/subastas-de-bienes-inmuebles-en-curso', headers=headers)

try:
    with urlopen(req) as mensaje:
        contenido_completo = mensaje.read().decode('utf-8')

    print("CONTENIDO COMPLETO DE LA URL:")
    print("=" * 60)
    print(contenido_completo)
    print("=" * 60)
    print(f"Longitud del contenido: {len(contenido_completo)} caracteres")

except Exception as e:
    print(f"Error: {e}")