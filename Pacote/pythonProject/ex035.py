soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('Todos os {} valores múltiplos de 3 tem a soma de {}'.format(cont, soma))