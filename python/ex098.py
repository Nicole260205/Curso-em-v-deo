from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
        print('-=' * 20)
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
        print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez: ')
ini = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor de fim: '))
pas = int(input('Digite o valor do passo: '))
contador(ini, fim, pas)