listanum = []
pares = []
impares = []
while True:
    listanum.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
for x, y in enumerate(listanum):
    if y % 2 == 0:
        pares.append(y)
    else:
        y % 2 == 1
        impares.append(y)
print(f'Foram digitados os seguintes valores {listanum}')
print(f'Os números pares são {pares}')
print(f'E os números impares são {impares}')