def notas(*num, sit=False):
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num) / len(num)

    if sit:
        if r['média'] >= 7:
            r['média'] = 'BOA'
        elif r['média'] >= 5:
            r['média'] = 'RAZOÁVEL'
        else:
            r['média'] = 'RUIM'

    return r

resp = notas(5.5, 9.5, 10, 6.5,sit=True)
print(resp)
    
