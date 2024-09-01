from random import randint

num = (randint(0,5), randint(0,5), randint(0,5), randint(0,5), randint(0,5))

maior = menor = num[0]

for c in num:
    if c > maior:
        maior = c
    if c < menor:
        menor = c


print(f'\nOs números sorteados foram: {num}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')