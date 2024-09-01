aluno = {}


aluno['nome'] = str(input('Nome: ')).title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] < 7:
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print('-='*30)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situação"]}')