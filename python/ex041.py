ano = int(input('Ano de nascimento: '))
idade = 2023 - ano

print('Sua idade é {}, então você é: '.format(idade))

if idade <= 9:
    print('Atleta Mirim')
elif idade >= 10 and idade <= 14:
    print('Atleta Infantil')
elif idade >= 15 and idade <= 19:
    print('Atleta Júnior')
elif idade >= 20 and idade <= 25:
    print('Atleta Sênior')
else:
    print('Atleta Master')