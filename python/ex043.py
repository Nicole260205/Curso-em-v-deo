peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em m? '))
imc = peso / altura ** 2

print('O IMC dessa pessoa é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso Ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')