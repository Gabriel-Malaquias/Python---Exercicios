numero = []
for cont in range(0,3):
    numero.append(int(input('Digite um valor: ')))
for p, n in enumerate(numero):
    print(f'Na posição {p} encontrei o valor {n}')

#OUTROS EXEMPLOS DE LISTA
x = [10, 11, 12, 13]
y = x[:]
y[3] = 20
print(x)
print(y)