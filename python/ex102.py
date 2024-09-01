def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        c = num
        f = 1
        while c > 0:
            print('{}'.format(c), end=' ')
            print('x ' if c > 1 else '=', end= '')
            f *= c
            c -= 1
        print(' {}'.format(f))
    else:
        return f


print(fatorial(5, show=True))

    

