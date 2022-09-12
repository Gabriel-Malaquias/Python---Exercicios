from random import randint
pc = randint(0,5)
print('----------------------------------------------------------')
print('VOU ESCOLHER UM NUMERO DE 0 A 5. QUERO VER VOCE ADVINHAR')
print('----------------------------------------------------------')
eu = int(input('Em qual numero eu pensei ? '))
if eu == pc:
    print('Voce Ganhou !')
else:
    print('Ihh otario, tu errou. Eu tava pensando no numero {} e nao no {}'.format(pc, eu))