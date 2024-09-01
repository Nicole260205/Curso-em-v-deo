from random import randint

lista = []
jogos = []

quant = int(input('Quantos jogos serão sorteados? '))
total = 1

while total <= quant:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'Jogo: {i+1}: {l}')