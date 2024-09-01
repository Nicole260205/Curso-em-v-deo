from random import randint
from time import sleep

numeros = []
def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0 
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    sleep(.5)
    print(f'Somando os valores pares de {lista}, temos {soma}')



sorteio(numeros)
somaPar(numeros)
