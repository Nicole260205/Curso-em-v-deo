def ficha(nome = '<desconhecido>' , goals= 0):
    print(f'O jogador {nome} marcou {goals} gols no campeonato. ')

n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Quantidade de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(goals=g)
else:
    ficha(n, g)
