pessoas = {}
lista = []
quantpessoas = 0
idades = []
mulheres = []

while True:
    pessoas['nome'] = str(input('Nome: ')).title()
    pessoas['sexo'] = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if pessoas['sexo'] not in 'FM':
        pessoas['sexo'] = str(input('Resposta inválida, tente novamente: ')).upper().strip()[0]
    if pessoas['sexo'] in 'F':
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = float(input('Idade: '))
    idades.append(pessoas['idade'])

    quantpessoas += 1

    media = sum(idades) / quantpessoas

    lista.append(pessoas.copy())

    resp = str(input(('Deseja continuar [S/N]: '))).upper().strip()[0]
    if resp in 'N':
        break
    if resp not in 'SN':
        resp = str(input('Resposta inválida, tente novamente: ')).upper().strip()[0]

print(f'- O grupo tem {quantpessoas} pessoas')
print(f'- A média de idade é de {media:.2f}')
print(f'- As mulheres cadastradas foram: {mulheres}')
for pessoa in lista:
    if pessoa['idade'] > media:
        print(pessoa)
