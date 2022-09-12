lista = [[], []]
valor = 0
for c in range(1,7):
    valor = int(input(f'Informe o {c}o valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Dos valores informados, os pares são {lista[0]}')
print(f'E os impares, são {lista[1]}')