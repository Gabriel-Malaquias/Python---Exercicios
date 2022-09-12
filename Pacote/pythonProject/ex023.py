print('------------------\nCONVERSAO DE BASES\n-------------------------')
v = int(input('Informe um valor: '))
print('''Selecione a opção sobre qual base deseja fazer a conversão:
[ 1 ] Base Binária
[ 2 ] Base Octal
[ 3 ] Base Hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('O valor {} em Binário é {}'.format(v,bin(v)[2:]))
elif op == 2:
    print('O valor {} em Octal é {}'.format(v, oct(v)[2:]))
elif op == 3:
    print('O valor {} em Hexadecimal é {}'.format(v, hex(v)[2:]))
else:
    print('Opção inválida')

