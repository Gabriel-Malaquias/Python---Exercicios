print('-=-=-=-=-=-= \n \033[35mTABUADA\033[m \n-=-=-=-=-=-=')
v = int(input('Digite um numero: '))
for c in range(0, 10 + 1):
    print('{} X {} = {}'.format(v, c, v*c))