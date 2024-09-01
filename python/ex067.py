num = 0
c = 0

while True:
    num = int(input('Quer ver a tabuada de que número? '))
    if num < 0: 
        break
    for c in range(0, 10):
        c += 1
        m = num * c
        print(f'{num} x {c} = {m}')
print('FIM')