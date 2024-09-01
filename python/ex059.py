n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opção = 0

while opção != 5:
    print('''De acordo com o seguinte menu, escolha a operação:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    opção = int(input('Qual a opção desejada: '))

    if opção == 1:
        soma = n1 + n2
        print('\nA soma dos números {} e {} é {}\n\n'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('\nA multiplicação dos números {} e {} é {}\n\n'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            print('\nO maior número é: {}\n\n'.format(n1))
        elif n2 > n1:
            print('\nO maior número é:{}\n\n'.format(n2))
        else:
            print('\nOs dois números são iguais!\n\n')
    elif opção == 4:
        print('\n\nInforme os números novamente: ')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif opção == 5:
        print('\nSaindo do programa!!!')
    else:
        print('\nOpção Inválida, escolha novamente')

print('\nFim do programa!')