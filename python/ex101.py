from datetime import datetime
anohoje = datetime.now().year

def voto(idade):
    if 16 <= idade < 18 or idade >= 70:
        return 'Opcional'
    elif 18 <= idade < 70:
        return 'Obrigatório'
    else:
        return 'Negado'

num = int(input('Informe o ano que você nasceu: '))

idade = anohoje - num

print(f'Com {idade} anos: Voto {voto(idade)}')