num = 0
soma = 0
c = 0

while num != 999:
    num = int(input('Informe um valor: '))
    if num != 999:
        c += 1
        soma += c

print('Foram digitidos {} números, e a soma é igual a {}'.format(c, soma))