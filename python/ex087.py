matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceiracoluna = 0
maior = menor = 0

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

for l in range(0,3):
    terceiracoluna += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maior =menor = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[1][c] < menor:
            menor = matriz[1][c]


print(f'\nA soma dos números pares é: {pares}', end=' ')
print(f'\nA soma da terceira coluna é: {terceiracoluna}', end=' ')
print(f'\nO maior valor da segunda linha é: {maior}', end=' ')
