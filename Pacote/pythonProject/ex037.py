#SOMA DE VALORES PARES DE 1 ATE 6
soma = 0
cont = 0
for c in range(1, 7):
    v = int(input('Informe um valor: '))
    if v % 2 == 0:
       soma = soma + v
       cont = cont + 1
print('Dos valores digitados, foram {} numeros \033[4;32mPARES\033[m e a soma entre eles foi {}'.format(cont, soma))