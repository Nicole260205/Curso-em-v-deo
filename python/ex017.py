from math import sqrt

oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))

hipotenusa = sqrt(oposto ** 2 + adjacente ** 2)

print('Com o cateto oposto sendo {} e o cateto adjacente sendo {}, a hipotenusa é igual á {:.2f}'.format(oposto, adjacente, hipotenusa))