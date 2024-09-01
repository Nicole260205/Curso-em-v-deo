num = 1
soma = 0
cont = 0
maior = 0
menor = 0
r = 'S'

while r == 'S':
    num = int(input('Informe um valor: '))
    r = str(input('Deseja continuar [N/S]: ')).strip().upper()
    if num != 0:
        cont += 1
        soma += num
        media = soma / cont
        if num == 1:
            menor = num
            maior = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

print('O menor número foi: {}'.format(menor))
print('O maior número fi: {}'.format(maior))
print('A média entre os números foi de: {}'.format(media))