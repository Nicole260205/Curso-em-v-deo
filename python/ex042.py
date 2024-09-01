r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 == r2 == r3:
    print('Esse triângulo é EQUILÁTERO')
elif r1 != r2 != r3:
    print('Esse triângulo é ESCALENO')
else:
    print('Esse triângulo é ISÓSCELES')
