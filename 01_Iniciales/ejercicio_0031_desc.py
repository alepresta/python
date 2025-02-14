print('-------------------------------------------------------------')
print('*************** TICKET COMPRA *******************************')
print('-------------------------------------------------------------')

precio_leche = float(input('Precio leche:     -->   '))
precio_pan =   float(input('Precio pan:       -->   '))
lechuga =      float(input('Precio lechuga:   -->   '))
precio_banana =   float(input('Precio banana:    -->   '))
descuento_porcentaje= int(input('¿Quieres aplicar algún descuento?: ---> n° --->   '))

subtotal = precio_leche +precio_pan + lechuga + precio_banana
descuento = subtotal * (descuento_porcentaje/100)
impuesto = subtotal * 0.21

print(f'''
leche: ${precio_leche}
pan: ${precio_pan}
lechuga: ${lechuga}
banana: ${precio_banana}
------------------------------
total sin descuento: ${subtotal} 
total con descuento %{descuento_porcentaje}: ${(subtotal-descuento):.2f}
total con impuesto %21: {((subtotal-descuento) * 1.21):.2f}

''')















