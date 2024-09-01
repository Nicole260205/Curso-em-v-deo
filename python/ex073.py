times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América', 'EC Vitória', 'Paraná')

cincoprimeiro = times[:5]
quatroultimos = times [-4:]
ordem = sorted(times)
chapecoense = times.index('Chapecoense')



print(f'Os 5 primeiros times: {cincoprimeiro}')
print(f'Os últimos 4 colocados: {quatroultimos}')
print(f'Times em ordem alfabética: {ordem}')
print(f'Em que posição está o time da Chapecoense: {chapecoense}º')