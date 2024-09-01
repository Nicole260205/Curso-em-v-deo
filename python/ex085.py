temp = [[], []]


for c in range(1, 8):
    num = (int(input(f'Digite o {c} valor: ')))

    if num % 2 == 0:
        temp[0].append(num)
    else:
        temp[1].append(num)

temp[0].sort()
temp[1].sort()
print(temp)
print(temp[0])
print(temp[1])