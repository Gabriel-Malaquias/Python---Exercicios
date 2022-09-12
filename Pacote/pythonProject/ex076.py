matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = col3 = maior = 0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite um valor para a posição [{c}, {l}]: '))
print('-='*30)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]',end='')
        if matriz[c][l] % 2 == 0:
            pares += matriz[c][l]
    print()
print('-='*30)
print(f'A soma dos valores pares da matriz foi {pares}')
for c in range(0,3):
    col3 += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {col3}')
for l in range(0,3):
    if l == 0:
        maior = matriz[1][l]
    elif matriz[1][l] > maior:
        maior = matriz[1][l]
print(f'Por ultimo, o maior valor da segunda linha é {maior}')