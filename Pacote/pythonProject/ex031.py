from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''' OPÇÕES
[ 0 ] \033[31mPedra\033[m
[ 1 ] \033[31mPapel\033[m
[ 2 ] \033[31mTesoura\033[m''')
jogador = int(input('\033[4mEscolha uma opção\033[m '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('='*30)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
print('='*30)
if computador == 0: #computador joga PEDRA
    if jogador == 0:
        print('\033[34mEMPATE\033[m')
    elif jogador == 1:
        print('\033[34mVOCÊ VENCEU\033[m')
    elif jogador == 2:
        print('\033[34mO PC VENCE\033[m')


elif computador == 1: #computador joga TESOURA
    if jogador == 0:
        print('\033[34mO PC VENCE\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE\033[m')
    elif jogador == 2:
        print('\033[34mVOCÊ VENCEU\033[m')


elif computador == 2: #computador joga PAPEL
    if jogador == 0:
        print('\033[34mVOCÊ VENCEU\033[m')
    elif jogador == 1:
        print('\033[34mO PC VENCE\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE\033[m')

