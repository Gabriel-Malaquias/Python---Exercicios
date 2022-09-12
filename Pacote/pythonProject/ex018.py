a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#valores menores
menor = a
if b < a and b < a:
    menor = b
if c < a and c < b:
    menor = c
#valores maiores
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Dos valore digitados, o menor é o {}'.format(menor))
print('Dos valore digitados, o maior é o {}'.format(maior))