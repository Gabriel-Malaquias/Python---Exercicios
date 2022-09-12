def fatorial(num):
    x = 1
    for c in range(num, 0, -1):
        print(f'{c} ', end='')
        if c > 1:
            print('x',end=' ')
        else:
            print('=',end=' ')
        x *= c
    return x


print(fatorial(5))