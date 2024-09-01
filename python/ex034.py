salario = float(input('Informe seu salário: R$'))

if salario > 1250:
    aumento = salario * 0.10
    total = salario + (salario + aumento)
    print('Seu salário aumentou de R${} para R${}, tendo um aumento de R${}'.format(salario, total, aumento))
else:
    aumento2 = salario * 0.15
    total2 = salario + (salario + aumento2)
    print('Seu salário aumentou de R${} para R${}, tendo um aumento de R${}'.format(salario, total2, aumento2))
