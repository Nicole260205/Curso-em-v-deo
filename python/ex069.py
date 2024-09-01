maiordeidade = 0
homem = 0
mulheres20 = 0

while True:
    idade = int(input('Sua idade: '))

    if idade >= 18:
        maiordeidade += 1
    
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Seu sexo [M/F]: ')).upper().strip()[0]

        if sexo == 'M':
            homem += 1

        if idade < 20 and sexo == 'F':
            mulheres20 += 1


    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Maior de idade: {maiordeidade}')
print(f'Homens: {homem}')
print(f'Mulheres menos de 20 anos: {mulheres20}')