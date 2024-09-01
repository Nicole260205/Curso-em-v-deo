num = []
contador = 0

while True:
    valor = int(input('Digite um valor: '))
    num.append(valor)
    contador += 1
    continuar = ' '
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break


num.sort(reverse=True)
print(f'Números digitados: {contador}')
print(f'Números em ordem decrescente : {num}')

if 5 in num:
    print('O número 5 está presente nessa lista!')
else:
    print(f'O número 5 não está presente nessa lista!')