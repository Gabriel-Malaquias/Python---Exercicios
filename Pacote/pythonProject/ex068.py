lista = []
while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
        print('Número adicionado')
    else:
        print('Número repetido, nao será adicionado')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Foram informados valores na seguinte ordem {lista}')