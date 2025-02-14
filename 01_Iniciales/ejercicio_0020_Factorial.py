# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120


def factorial(numero):
    if numero == 1:
        return 1
    else:
        return  numero * factorial(numero-1)

numero = 3


print(f'Factorial de: {numero}! = {factorial(numero)}' )