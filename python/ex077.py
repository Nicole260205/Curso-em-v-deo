palavras = ('Harry', 'Louis','Niall', 'Zayn', 'Liam', 'Taylor', 'Luke', 'Michael', 'Callum', 'Ashton', 'Lewis', 'Conan')

for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos', end= ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

