distancia = float(input('Qual a distância de sua viagem em km?: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da passagem será de R${} para a quantidade {} de km'.format(valor, distancia))
else:
    valor2 = distancia * 0.45
    print('O valor da passagem será de R${} para a quantidade {} de km'.format(valor2, distancia))
