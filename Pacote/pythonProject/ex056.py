total = total1 = cont = menor = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Informe o preço do produto R$: '))
    cont += 1
    total = total + preço
    if preço > 1000:
        total1 += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer comtinuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'No total, foi gasto R${total}')
print(f'Existem {total1} produtos acima de R$1000,00')
print(f'O produto mais barato foi {barato} de {menor}R$')