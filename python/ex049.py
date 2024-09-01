num = int(input('Digite um número: '))


for c in range( 0, 11):
    tabuada = c * num
    print('{} x {:2} = {}'. format(c, num, tabuada))