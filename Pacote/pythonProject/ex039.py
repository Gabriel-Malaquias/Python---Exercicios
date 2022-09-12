print('====================== \n \033[31mDETERCTOR DE POLÍNDROMO\033[m   \n =======================')
frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um políndromo')
else:
    print('Essa frase não é um políndromo')