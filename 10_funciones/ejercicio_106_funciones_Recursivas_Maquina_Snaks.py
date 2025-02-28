print('************* Cálculo de impuestos *************')

def calcular_impuesto(monto,impuesto):
    pago_total = monto + monto * (impuesto/100)
    return pago_total

monto = float(input(f'Ingrese el monto sin impuesto: -> '))
impuesto = float(input(f'Ingrese % impuesto (1% a 100%): -> '))

total = calcular_impuesto(monto,impuesto)
print(f'Pago con impuesto: ${total:.2f}')

