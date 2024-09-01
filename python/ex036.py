valorCasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
anos = float(input('Informe em quantos anos você irá pagar: '))

parcela = valorCasa / (anos * 12) 

print('Você terá que pagar {:.2f} por mês por {} anos'.format(parcela, anos))

if parcela >= (salario * 0.30):
    print('Você não é permitido comprar essa casa!')
else:
    print('Parabéns! Você pode comprar a casa')