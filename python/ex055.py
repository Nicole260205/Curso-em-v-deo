maior = 0
menor = 0 

for i in range(1, 6):
    peso = float(input('Informe peso da {}º pessoa: '.format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso: {}'.format(maior))
print('O menor peso: {}'.format(menor))