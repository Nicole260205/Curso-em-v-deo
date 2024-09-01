total = 0
preçomaisquemil = 0
menorpreço = 0
contador = 0
maisbarato = ' '

while True:

    nome = str(input('Nome do produto: ')).strip()

    preço = float(input('Preço do produto: R$'))

    contador += 1
    total += preço

    if preço > 1000:
        preçomaisquemil += 1

    if contador == 1:
        menorpreço = preço
        maisbarato = nome
    else:
        if preço < menorpreço:
            menorpreço = preço
            maisbarato = nome

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break



print(f'qual é o total gasto na compra: {total}')
print(f'quantos produtos custam mais de R$1000: {preçomaisquemil}')
print(f'qual é o nome do produto mais barato: {maisbarato}')