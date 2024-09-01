preço = float(input('Preço das compras:'))
print('''Formas de pagamento
      [1] À vista dinheiro/cheque
      [2] À vista no cartão
      [3] Em até 2x no cartão
      [4] 3x ou mais no cartão''')
opção = int(input('Qual a forma de pagamento: '))

if opção == 1:
    novoPreço = preço - (preço - 0.10)
elif opção == 2:
    novoPreço = preço - (preço - 0.5)
elif opção == 3:
    novoPreço = preço
    parcela = novoPreço / 2
    print('Sua compra foi parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    novoPreço = preço + (preço * 0.20)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = novoPreço / totalParcelas
    print('Sua compra foi parcelada em {}x de R${:.2f}'.format( totalParcelas,parcela))
else:
    print('Opção Invalida')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, novoPreço))