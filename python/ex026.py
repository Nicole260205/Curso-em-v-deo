frase = str(input('Digite uma frase: ')).upper().strip


print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira letra "A" apareceu primeiro na posição {}'.format(frase.find('A') + 1))
print('A ultima letra "A" apareceu pela ultima vez na posição {}'.format(frase.rfind('A') + 1))
