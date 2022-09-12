lista = []
menor = 0
maior = 0
for c in range (0,5):
    lista.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista [c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista foi {maior} na posição ', end='')
for x, y in enumerate(lista):
    if y == maior:
        print(f'{x}')
print(f'O menor valor da lista foi {menor} na posição ',end='')
for x, y in enumerate(lista):
    if y == menor:
        print(f'{x}')