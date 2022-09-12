print('-='*10)
print('ANALISANDO UM TRIANGULO')
print('-='*10)
reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informa o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores informados FORMAM um triangulo')
else:
    print('Os valores informados NÃO FORMAM um triangulo')
