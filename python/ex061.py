c = 1
a = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

while c <= 10:
    pa = a + (c - 1) * r
    c += 1
    print(pa, end=' ')