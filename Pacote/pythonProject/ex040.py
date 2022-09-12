print('='*20)
print('\033[34mGRUPO DA MAIORIDADE\033[m')
print('='*20)
contmaior = 0
contmenor = 0
from datetime import date
for c in range(1, 8):
    nasc = int(input('Ano de nascimento da {} pessoa: '.format(c)))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        contmaior = contmaior + 1
    else:
        idade < 18
        contmenor = contmenor + 1
print('O total de pessoas maiores de idade são {}'.format(contmaior))
print('O total de pessoas menores de idade é {}'.format(contmenor))