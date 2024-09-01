num = 0
c = 0
soma = 0

while True:
    num = int(input('Informe um valor: '))
    if num == 999:
        break
    c += 1
    soma += num

print(f'Foram usados {c} números e a soma é {soma}')