#METODO 1:
from math import factorial
num = int(input('Digite um numero para saber seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num,f))

#METODO 2:
num = int(input('Digite um número para saber seu fatorial: '))
c = num
f = 1
print('CALCULANDO {}! = '.format(num),end='')
while c > 0:
   print('{}'.format(c), end='')
   print(' x 'if c > 1 else ' = ',end='')
   f = f * c
   c = c - 1
print('{}'.format(f),end='')

