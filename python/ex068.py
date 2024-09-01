from random import randint
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if opcao == 'P':
        if total % 2 == 0:
            print('Você GANHOU!!!')
            v += 1
        else: 
            print('Você PERDEU!!!')
            break
    else:
        if total % 2 == 1:
            print('Você GANHOU!!!')
            v += 1
        else: 
            print('Você PERDEU!!!')
            break

print(f'Você ganhou {v} vezes')