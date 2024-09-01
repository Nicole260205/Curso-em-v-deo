valores = []
maior = menor = 0

for c in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {c}: '))
    valores.append(valor)

    if c == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição {valores.index(maior)} ')
print(f'O menor valor digitado foi {menor} na posição {valores.index(menor)} ')
