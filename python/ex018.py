import math

angulo = float(input('Digite um ângulo qualquer: '))

radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}' .format(cosseno))
print('Tangente: {:.2f}' .format(tangente))