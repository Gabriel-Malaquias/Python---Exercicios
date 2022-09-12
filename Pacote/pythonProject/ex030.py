print('{:=^60}'.format(' \033[36mLOJA DE ELETRONICOS\033[m '))
preço = float(input('Qual o preço do produto ? '))
print('''QUAL SERÁ A FORMA DE PAGAMENTO ?
[ 1 ] À VISTA/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opção = int(input('\033[31mSELECIONE UMA OPÇÃO\033[m: '))
if opção == 1:
    total = preço - (10/100 * preço)
elif opção == 2:
    total = preço - (5/100 * preço)
elif opção == 3:
    total = preço
    parcela = preço /2
    print('Dividido em 2x, cada parcela terá um valor de {}'.format(parcela))
elif opção == 4:
    total = preço + (20/100 * preço)
    numparc = int(input('Quantas parcelas ? '))
    parcelas = total / numparc
    print('Cada parcela terá um valor de R${:3}'.format(parcelas))
print('Sua compra foi de R${} e terá que pagar um valor final de R${}'.format(preço,total))

