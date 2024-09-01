import random

numero = random.randint(0, 5)

tentativa = int(input('Tente adivinhar o número entre 0 e 5: '))
if tentativa == numero:
    print('Parabéns, você acertou')
else:
    print('Errado, o número certo era {}'.format(numero))