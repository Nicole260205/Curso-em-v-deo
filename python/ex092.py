cadastro = {}
lista = []
ano = 2023

cadastro['nome'] = str(input('Nome: ')).title()
cadastro['nascimento'] = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['anodecontratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))

idade = ano - cadastro['nascimento']
cadastro['nascimento'] = idade
aposentadoria = 35 + (ano - cadastro['anodecontratação'])
cadastro['anodecontratação'] = aposentadoria

lista.append(cadastro.copy())
print(cadastro)

for e in lista:
    for k, v in e.items():
        print(f'{k} tem o valor {v}')