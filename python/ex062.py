c = 1
a = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

while c <= 10:
    pa = a + (c - 1) * r
    c += 1
    print(pa, end=' ')

print('Pausa')
mais = int(input('Quantos termos você deseja ver a mais?  '))

while mais != 0:
    c_aux = 1
    while c_aux <= mais:
        pa = a + (c - 1) * r
        print(pa, end=' ')
        c += 1
        c_aux += 1
    mais = int(input('Quantos termos você deseja ver a mais?  '))

print('Programa encerrado.')
