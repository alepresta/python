def totalDeUnPago(pago:int, impuesto:int):
    pagoconImpuesto = pago +  pago * (impuesto/100)
    return pagoconImpuesto

pago = float(input(f'Ingrese Importe sin impuestos --> '))
impuesto = float(input(f'Ingrese porcentaje de impuesto --> '))

total = totalDeUnPago(pago,impuesto)

print(f'Monto: ${pago}, Impuesto: {impuesto}% = Total: ${total}')
