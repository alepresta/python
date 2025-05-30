print('************************** Manejo de archivos ***************************')
print('********  doc, txt,xls,mp3, csv, dll,vob,rar, jpg,png,exe,html **********')
archivo = None  # Initialize archivo to None
try:
    archivo = open('prueba.txt','w', encoding='utf8')
    archivo.write(f'Agregamos información al archivo\n')
    archivo.write('Adiós!\n')
except Exception as e:
    print(e)
finally:
    if archivo is not None:  # Check if archivo was successfully opened
        archivo.close()

