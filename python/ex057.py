sexo = str(input('Informe seu sexo [F/M]: ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos, tente novamante: ')).upper().strip()[0]

print('{} registrado'.format(sexo))