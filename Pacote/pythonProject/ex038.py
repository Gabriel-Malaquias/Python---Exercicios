num = int(input('Digite um numero: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ') #PAR
        total = total + 1
    else: #IMPAR
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n \033[mO número {} foi divido {} vezes\033[m'.format(num, total))
if total == 2:
    print('Portanto, é um número \033[33mPRIMO\033[m')
else:
    print('Portanto, ele \033[33mNÃO É PRIMO\033[m')

