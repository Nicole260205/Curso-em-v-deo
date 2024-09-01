n1 = int(input('Insire o primeiro valor: '))
n2 = int(input('Insire o segundo valor: '))
n3 = int(input('Insire o terceiro valor: '))
n4 = int(input('Insire o quarto valor: '))

numeros = (n1, n2, n3, n4)

numero9 = numeros.count(9)
primeiro3 = numeros.index(3) + 1 if 3 in numeros else 0
numeropar = [c for c in numeros if c % 2 == 0]

print(f'Quantas vezes apareceu o valor 9: {numero9}')
print(f'Em que posição foi digitado o primeiro valor 3: {primeiro3}')
print(f'Quais foram os números pares: {numeropar}')