# def sumarValores(*args):
#     valores =  sum(args)
#     return valores


def sumarValores(*args):
    pass
    result = 0
    for valor in args:
        result += valor
    return result




valorA = 10
valorB = 1
valorC = 2
valord = 4

print(f'{valorA} + {valorB} + {valorC} + {valord} + 10 = {sumarValores(valorA,valorB,valorC,valord,10)}')



