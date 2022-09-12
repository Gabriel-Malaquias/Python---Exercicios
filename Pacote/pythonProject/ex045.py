print('-='*6)
print('ADVINHÇÃO')
print('-='*6)
from random import randint
palpites = 0
pc = randint(0,10)
eu = int(input('Em qual numero eu pensei ? '))
while pc != eu:
    eu = int(input('Tente Novamente: '))
    palpites += 1
    if eu < pc:
        print('Tá \033[33mquente\033[m...')
    else:
        eu > pc
        print('Tá \033[34mfrio\033[m...')
print('Voce acertou. Foi necessário {} palpites para voce advinhar'.format(palpites))
