km = float(input('Qual a quantidade de km percorrido: '))
dias = float(input('Por quantos dias o carro foi alugado: '))
preco = (dias * 60) + (km * 0.15)
print('O preço pelo carro que percorreu {}km em {} dias é de: R${:.2f}' .format(km, dias, preco))