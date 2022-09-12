val = int(input('Digite um número: '))
uni = val // 1 % 10
dez = val // 10 % 10
cen = val // 100 % 10
mil = val // 1000 % 10
print('Unidade {} \n Dezena {} \n Centena {} \n Milhar {}'.format(uni, dez, cen, mil))
