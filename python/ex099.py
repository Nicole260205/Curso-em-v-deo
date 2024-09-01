def maior(*num):
        maior = menor = num[0]
        for i in num:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
        print(f'Números: {num}. Foram informados {len(num)} valores ao todo')
        print(f'O maior número foi {maior}')




maior(1, 2, 3, 4, 5)
maior(6, 8, 3)