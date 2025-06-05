print('************************** Clase Manejo de archivos ***************************')

class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reader = None # Para almacenar el objeto PdfReader

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        try:
            self.reader = PdfReader(self.nombre)
            # Retornamos el objeto PdfReader para que puedas acceder a sus métodos
            return self.reader
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")
            self.reader = None # Asegurarse de que no quede un reader inválido
            raise # Volver a lanzar la excepción para que el 'with' la maneje

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50, '-'))
        # No necesitas cerrar explícitamente el lector de pypdf como un archivo normal,
        # ya que pypdf maneja la lectura del archivo internamente.
        # El 'with' statement se encarga de que los recursos subyacentes se liberen.
        if tipo_excepcion:
            print(f"Se produjo una excepción: {tipo_excepcion}, {valor_excepcion}, {traza_error}")

# Uso del manejador de contexto
try:
    with ManejoArchivos('libro.pdf') as pdf_reader:
        if pdf_reader: # Verificar si el lector de PDF se creó correctamente
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                print(f"\n--- Contenido de la página {page_num + 1} ---")
                print(page.extract_text())
        else:
            print("No se pudo leer el archivo PDF.")
except FileNotFoundError:
    print("Error: El archivo 'libro.pdf' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

