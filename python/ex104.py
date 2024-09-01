def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('Erro!!! Digite um número inteiro: ')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')