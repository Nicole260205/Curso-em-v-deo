num = []
pares = []
impar = []

while True:
    valor = int(input('Digite um valor: '))
    num.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
    continuar = ' '
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
    

print(f'Todos os números: {num}')
print(f'Pares: {pares}')
print(f'Impares: {impar}')