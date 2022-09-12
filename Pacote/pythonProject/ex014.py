print('---------------- \n ORÇAMENTO DA EMPRESA \n -----------------')
nome = str(input('Nome do funcionário: '))
sal = float(input('Salário de {}: '.format(nome)))
sup = 1250
if sal > sup:
    ns1 = (10/100) * sal + sal
    print('O novo salário deste funcionario será {}'.format(ns1))
else:
    sal < sup
    ns2 = (15/100) * sal + sal
    print('O novo salário deste funcionario será {}'.format(ns2))


