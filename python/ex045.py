from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Escolha sua jogada: '))

print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador ganhou!')
    elif jogador == 2:
        print('Computador ganhou!')
    else:
        print('Opção Invalida!')

elif computador == 1:
    if jogador == 0:
        print('Computador ganhou!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganhou!')
    else:
        print('Opção Invalida!')

elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou!')
    elif jogador == 1:
        print('Computador ganhou!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção Invalida!')