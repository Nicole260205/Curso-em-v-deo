import math

velocidade = int(input('Insire a velocidade do carro em km/h: '))

if velocidade > 80:
    excessoUltrapassado = velocidade - 80
    multa = excessoUltrapassado * 7
    print('Você está acima da velocidade! A multa será de R${} pois você estava {}km acima da velocidade permitida'.format(multa, excessoUltrapassado))
else:
    print("Velocidade dentro do limite. Dirija com segurança!")
