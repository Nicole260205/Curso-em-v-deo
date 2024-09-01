n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

print('As notas foram {} e {} com a média de {}'.format(n1, n2, media))
if media < 5:
    print('Aluno reprovado')
elif media >= 5 and media <= 6.9:
    print('Aluno em recuperação')
else:
    print('Aluno aprovado')