lista = []
cont = 0
while True:
    lista.append(int(input('Informe um numero: ')))
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram digitados {cont} valores')
lista.sort(reverse=True)
print(f'A ordem decrescente dos valores é {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print(f'O valor 5 não está na lista')