print('-='*10)
print('\033[31mBALANÇA DE PESO\033[m')
print('-='*10)
for c in range(1, 6):
    peso = float(input('Peso da pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))


