ano = int(input('Ano de nascimento: '))
idade = 2023 - ano

if idade < 18:
    tempo = 18 - idade
    print('Você ainda não tem idade pra se alistar, aindam faltam {} anos'.format(tempo))
elif idade == 18:
    print('Você está na idade de se alistar')
else:
    tempo2 = idade - 18
    print('Você já passou da idade de se alistar, você deveria ter se alistado há {} anos'.format(tempo2))