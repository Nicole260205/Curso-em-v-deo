somaIdade = 0
media = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulheres = 0

for p in range( 1, 5):
    print('--{} pessoa --'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mn':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulheres += 1

media = somaIdade / 4
print('A media de idade do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulheres))

