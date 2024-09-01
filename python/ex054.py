ano = 2023
maiorIdade = ano - 21
c = 0
cc = 0

for i in range(1, 8):
    idade = int(input('Ano de nascimento: '))
    if idade > maiorIdade:
        c += 1
    else:
        cc += 1
print('Maiores de idade: {}'.format(c))
print('Menores de idade: {}'.format(cc))