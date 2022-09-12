n = (int(input('Informe um número: ')),
    int(input('Informe um número: ')),
    int(input('Informe um número: ')),
    int(input('Informe um número: ')))
print(f'Os valores digitados foram {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 aparece na posição {n.index(3)+1}')
else:
    print('O 3 nao aparece')
print('Os numero pares foram', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')