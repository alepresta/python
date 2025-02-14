#set
planetas = { 'Marte', 'Júpiter', 'Venus'}

print(planetas)
print(len(planetas))
print('Marte' in planetas)
print('Martes' in planetas)
planetas.add('Tierra')
print(planetas)
planetas.add('Tierra')
planetas.remove('Tierra')
#planetas.remove('Tierras')  #ERROR
planetas.discard('Tierras')  #SI ERROR
print(planetas)
planetas.clear()
del planetas