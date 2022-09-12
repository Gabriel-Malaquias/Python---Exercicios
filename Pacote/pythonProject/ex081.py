from random import randint
from operator import itemgetter
from time import sleep
ordem = ()
test = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint (1,6)}
for x, y in test.items():
    print(f'{x} jogou {y} no dado')
    sleep(1)
print('='*40)
ordem = sorted(test.items(), key=itemgetter(1), reverse=True)
print('<<<<< \033[31mRANKING DOS JOGADORES\033[m >>>>>>')
for x, y in enumerate(ordem):
    print(f'{x+1} lugar: {y[0]} lançou {y[1]} no dado')
    sleep(1)