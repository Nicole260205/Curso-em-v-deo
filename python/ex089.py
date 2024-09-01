alunos = []
temp = []
p = 0

while True:
    nome = str(input('Nome: ')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    temp.append(nome)
    temp.append([n1, n2])

    alunos.append(temp[:])
    temp.clear()
    
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

print('-='*30)
print('BOLETIM')
for i, aluno in enumerate(alunos, 1):
    print(f'{i}º Aluno: {aluno[0]} - Média: {sum(aluno[1]) / len(aluno[1]):.2f}')

while True:
    p = int(input('Qual aluno deseja ver as notas: '))
    if p == 999:
        break
    elif 1 <= p <= len(alunos):
        aluno_escolhido = alunos[p - 1]
        print(f'Aluno: {aluno_escolhido[0]}, Notas: {aluno_escolhido[1]}')
    else:
        print('Aluno não encontrado. Tente novamente.')



