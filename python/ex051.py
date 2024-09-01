a = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

for n in range(1, 11):
    pa = a + (n - 1) * r
    print(pa, end=' ')