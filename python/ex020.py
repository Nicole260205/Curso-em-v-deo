import random

aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')

sorteio = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteio)

print('A ordem será: ')
print(sorteio)