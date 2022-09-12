dado = []
lista = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso(Kg): ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar ? '))
    if resp in 'Nn':
        break
print(f'No total foram cadastradas {len(lista)} pessoas')
print(f'O maior peso cadastrado foi de {maior}, sendo de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'E o menor peso cadastrado foi de {menor}, sendo de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}')