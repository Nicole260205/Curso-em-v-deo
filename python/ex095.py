lista = []

while True:
    jogadores = {}
    jogadores['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))

    goals = []  
    for i in range(partidas): 
        goals.append(int(input(f'Quantos gols na partida {i + 1}: ')))
    jogadores['goals'] = goals
    total = sum(goals)
    jogadores['total'] = total

    lista.append(jogadores.copy())
    resp = str(input(('Deseja continuar [S/N]: '))).upper().strip()[0]
    if resp in 'N':
        break
    if resp not in 'SN':
        resp = str(input('Resposta inválida, tente novamente: ')).upper().strip()[0]

print('-='*30)
print('cod ', end='')
for chave in lista[0].keys():
    print(f'{chave:<15}', end='')  
print()
print('-='*40)
for k, jogador in enumerate(lista):
    print(f'{k+1:>3}', end='')  
    for valor in jogador.values():
        print(f'{str(valor):<15}', end='')
    print()
print('-='*40)
