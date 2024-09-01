dados = []
informações = []
maiorpeso = menorpeso = 0 


while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    
    if len(informações) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]

    informações.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break

print(f'Ao todo, você cadastrou: {len(informações)} pessoas')
print(f'O maior peso foi de {maiorpeso}kg. Peso de: ', end=' ')
for p in informações:
    if p[1] == maiorpeso:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menorpeso}kg. Peso de: ', end=' ')
for p in informações:
    if p[1] == menorpeso:
        print(p[0], end=' ')
