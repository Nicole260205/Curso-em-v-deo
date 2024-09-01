from random import randint
palpites = 0

num = randint(0 , 10)

tentativa = int(input('Tente adivinhar o número entre 0 e 10: '))

while tentativa != num:
    print('ERROU...Tente novamente: ')
    palpites += 1
    tentativa = int(input('Tente adivinhar o número entre 0 e 10: '))


print('Exatamente, foi necessárias {} tentativas'.format(palpites + 1))