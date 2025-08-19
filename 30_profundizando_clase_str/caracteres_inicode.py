print(f' caracteres unicode '.center(40,'🦆'))

unicode_00 = '♛'
unicode_01 = '₿'
unicode_02 = '⁑'
unicode_03 = 'ὔ'
unicode_04 = '🦆'
unicode_05 = 'u\u2665'
unicode_06 = '\U0001f600'
unicode_07 = '\U0001f40D'
unicode_08 = '\U0001FAB7'

print('Hola \u0020Mundo \u0041 \u20bf \U000020bf \x41')
print(unicode_04, unicode_02, unicode_03, unicode_04, unicode_05, unicode_06, unicode_07, unicode_08)
print('')

print(f' caracteres ascii '.center(40,'■'))
ascii_al_cuadrado = chr(253)
ascii_potencia_tres = chr(252)
ascii_signo_de_seccin =  chr(245)
ascii_signo_de_calderon = chr(244)


ascii_00 = chr(65)
ascii_01 = chr(64)
print(f'Imprimir A maúscula: {ascii_00}')
print((f'Imprimir arroba: {ascii_01}'))
print(f'2{ascii_al_cuadrado}= 4')









