cinquenta = 0
vinte = 0
dez = 0
um = 0

valor_original = int(input('Valor a ser sacado: '))
num = valor_original  

if num >= 50:
    cinquenta = num // 50
    num %= 50

if num >= 20:
    vinte = num // 20
    num %= 20

if num >= 10:
    dez = num // 10
    num %= 10

if num >= 1:
    um = num // 1
    num %= 1

print(f'Valor fechado: {valor_original}')
print(f'50 -> {cinquenta}')
print(f'20 -> {vinte}')
print(f'10 -> {dez}')
print(f'1 -> {um}')
