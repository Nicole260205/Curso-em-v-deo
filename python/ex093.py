jogadores = {}
goals = []
total = 0
lista =[]

jogadores['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))
for i in range(partidas): 
    goals.append(int(input(f'Quantos gols na partida {i + 1}: ')))
jogadores['goals'] = goals
total = sum(goals)
jogadores['total'] = total

lista.append(jogadores.copy())
print('-='*30)
print(jogadores)
print('-='*30)
for e in lista:
    for k, v in e.items():
        print(f'{k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogadores["nome"]} jogou {partidas} jogos: ')
for i in range(partidas):
    print(f'Na partida {i + 1}, fez {jogadores["goals"][i]} gols')