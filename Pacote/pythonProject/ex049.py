print('='*20)
print('\033[31mSEQUENCIA FIBONACCI\033[m')
print('='*20)
v = int(input('Digite um valor: '))
a1 = 0
a2 = 1
print('{} -> {}'.format(a1, a2), end='')
cont = 3
while cont <= v:
    a3 = a1 + a2
    print('-> {}'.format(a3), end='')
    a1 = a2
    a2 = a3
    cont += 1