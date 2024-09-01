num = int(input('Escolha um número qualquer: '))
print('''Escolha uma base de conversão
[1] Binário 
[2] Octal 
[3] Hexadecimal''')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print('O número {} convertido para binário é: {}'.format(num, bin(num)))
elif escolha == 2:
    print('O número {} convertido para octal é: {}'.format(num, oct(num)))
elif escolha == 3:
    print('O número {} convertido para hexadecimal é: {}'.format(num, hex(num)))
else:
    print('Essa opção não é permitida')
