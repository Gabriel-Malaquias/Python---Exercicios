print('------------------------- \n MINHA CASA, MINHA VIDA !!! \n ---------------------------')
valorCs = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
prestações = float(input('Digite o número de parcelas desejadas para o financiamento ? '))
x = 30/100 * salario
if valorCs / (prestações * 12) < x:
    print('Impréstimo aprovado')
else:
    valorCs / (prestações * 12) > x
    print ('Impréstismo Negado')
