num = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado...')
    else: 
        print('Valor já adicionado anteriormente ')
    continuar = ' '
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break

    
num.sort()
print(f'Você digitou os valores {num}')